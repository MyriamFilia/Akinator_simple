from django.shortcuts import render, redirect
from .donnees import question_personnages, personnages, question_animaux, animaux, question_objets, objets
import random

# Constantes pour les clés de session
SESSION_POSSIBILITES = "possibilités"
SESSION_QUESTIONS_POSEES = "questions_posées"
SESSION_QUESTION_NUM = "question_num"

def accueil(request):
    """Page d'accueil du jeu."""
    request.session.flush()  # Réinitialiser la session
    return render(request, "index.html")

def theme(request):
    """Page des thèmes du jeu."""
    return render(request, "theme.html")

def obtenir_questions_par_theme(theme):
    """Retourne les questions et entités associées à un thème donné."""
    themes_data = {
        "personnages": (question_personnages, personnages),
        "animaux": (question_animaux, animaux),
        "objets": (question_objets, objets),
    }
    return themes_data.get(theme, ([], []))

def initialiser_possibilites(request, theme):
    """Initialise les possibilités dans la session en fonction du thème."""
    if SESSION_POSSIBILITES not in request.session or not request.session[SESSION_POSSIBILITES]:
        _, possibilites = obtenir_questions_par_theme(theme)
        request.session[SESSION_POSSIBILITES] = possibilites

def filtrer_possibilites(possibilites, question, reponse):
    """Filtre les possibilités en fonction de la réponse donnée."""
    attribut = question['attribut']
    if reponse == "oui":
        return [p for p in possibilites if p.get("attributs", {}).get(attribut, False)]
    return [p for p in possibilites if not p.get("attributs", {}).get(attribut, False)]

def jeu_akinator(request, theme):
    """Gère la logique principale du jeu."""
    # Initialisation des variables de session
    request.session.setdefault(SESSION_QUESTIONS_POSEES, [])
    request.session.setdefault(SESSION_QUESTION_NUM, 1)
    
    # Initialisation des possibilités et des questions
    initialiser_possibilites(request, theme)
    questions, _ = obtenir_questions_par_theme(theme)

    if request.method == "POST":
        # Gestion des réponses soumises
        question_id = int(request.POST['question_id'])
        reponse = request.POST['reponse']
        
        # Trouver la question et filtrer les possibilités
        question = next((q for q in questions if q["id"] == question_id), None)
        if question:
            request.session[SESSION_POSSIBILITES] = filtrer_possibilites(
                request.session[SESSION_POSSIBILITES], question, reponse
            )

        request.session[SESSION_QUESTIONS_POSEES].append(question_id)
        request.session[SESSION_QUESTION_NUM] += 1
        request.session.modified = True

        # Gestion des cas terminaux
        if not request.session[SESSION_POSSIBILITES]:
            return render(request, "resultat.html", {"nom": "Désolé je n'ai pas la réponse", "theme": theme})
        if len(request.session[SESSION_POSSIBILITES]) == 1:
            nom = request.session[SESSION_POSSIBILITES][0]['nom']
            return render(request, "resultat.html", {"nom": "Je pense que c'est " + nom , "theme": theme})

    # Sélection de la prochaine question
    remaining_questions = [q for q in questions if q["id"] not in request.session[SESSION_QUESTIONS_POSEES]]
    next_question = remaining_questions[0] if request.session[SESSION_QUESTION_NUM] == 1 else random.choice(remaining_questions) if remaining_questions else None

    return render(request, "questions.html", {
        "question": next_question,
        "theme": theme,
        "question_num": request.session[SESSION_QUESTION_NUM]
    })

def reinitialiser(request):
    """Réinitialise le jeu."""
    request.session.flush()
    return redirect('accueil')