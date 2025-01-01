
# Liste des questions
question_personnages = [
    {"id": 1, "texte": "Est-ce un personnage réel?", "attribut": "personnage"},
    {"id": 2, "texte": "Est-ce un homme ?", "attribut": "homme"},
    {"id": 3, "texte": "Est-ce un personnage d'anime ?", "attribut": "anime"},
    {"id": 4, "texte": "Est-ce un personnage de film ou série ?", "attribut": "film_serie"},
    {"id": 5, "texte": "Est-ce un acteur ou chanteur ?", "attribut": "acteur_chanteur"},
    {"id": 6, "texte": "Est-ce un personnage historique ?", "attribut": "historique"},
    {"id": 7, "texte": "Est-ce un personnage de dessin animé ?", "attribut": "dessin_anime"},
    {"id": 8, "texte": "Est-ce un personnage de jeu vidéo ?", "attribut": "jeu_video"},
    {"id": 9, "texte": "Est-ce un personnage de bande dessinée ?", "attribut": "bande_dessinee"},
    {"id": 10, "texte": "Est-ce un personnage de littérature ?", "attribut": "litterature"},
    {"id": 11, "texte": "Est-ce un personnage de mythologie ?", "attribut": "mythologie"},
    {"id": 12, "texte": "Est-ce un personnage de science-fiction ?", "attribut": "science_fiction"},
    {"id": 13, "texte": "Est-ce un personnage de fantasy ?", "attribut": "fantasy"},
    {"id": 14, "texte": "Est-ce un personnage de comédie ?", "attribut": "comedie"},
    {"id": 15, "texte": "Est-ce un personnage de drame ?", "attribut": "drame"},
    {"id": 16, "texte": "Est-ce un personnage de romance ?", "attribut": "romance"}
]

# Liste des personnages
personnages = [
   # Personnages connus
    {"nom": "Albert Einstein", "attributs": {"personnage": True, "homme": True, "anime": False, "film_serie": False, "acteur_chanteur": False, "historique": True, "dessin_anime": False, "jeu_video": False, "bande_dessinee": False, "litterature": False, "mythologie": False, "science_fiction": False, "fantasy": False, "comedie": False, "drame": False, "romance": False}},
    {"nom": "Marie Curie", "attributs": {"personnage": True, "homme": False, "anime": False, "film_serie": False, "acteur_chanteur": False, "historique": True, "dessin_anime": False, "jeu_video": False, "bande_dessinee": False, "litterature": False, "mythologie": False, "science_fiction": False, "fantasy": False, "comedie": False, "drame": False, "romance": False}},
    {"nom": "Nelson Mandela", "attributs": {"personnage": True, "homme": True, "anime": False, "film_serie": False, "acteur_chanteur": False, "historique": True, "dessin_anime": False, "jeu_video": False, "bande_dessinee": False, "litterature": False, "mythologie": False, "science_fiction": False, "fantasy": False, "comedie": False, "drame": True, "romance": False}},
    {"nom": "Mère Teresa", "attributs": {"personnage": True, "homme": False, "anime": False, "film_serie": False, "acteur_chanteur": False, "historique": True, "dessin_anime": False, "jeu_video": False, "bande_dessinee": False, "litterature": False, "mythologie": False, "science_fiction": False, "fantasy": False, "comedie": False, "drame": False, "romance": False}},

    # Personnages d'anime
    {"nom": "Naruto Uzumaki", "attributs": {"personnage": False, "homme": True, "anime": True, "film_serie": False, "acteur_chanteur": False, "historique": False, "dessin_anime": True, "jeu_video": True, "bande_dessinee": True, "litterature": False, "mythologie": False, "science_fiction": False, "fantasy": True, "comedie": False, "drame": True, "romance": False}},
    {"nom": "Luffy", "attributs": {"personnage": False, "homme": True, "anime": True, "film_serie": False, "acteur_chanteur": False, "historique": False, "dessin_anime": True, "jeu_video": True, "bande_dessinee": True, "litterature": False, "mythologie": False, "science_fiction": False, "fantasy": True, "comedie": True, "drame": False, "romance": False}},
    {"nom": "Sakura Haruno", "attributs": {"personnage": False, "homme": False, "anime": True, "film_serie": False, "acteur_chanteur": False, "historique": False, "dessin_anime": True, "jeu_video": True, "bande_dessinee": True, "litterature": False, "mythologie": False, "science_fiction": False, "fantasy": True, "comedie": False, "drame": False, "romance": True}},
    {"nom": "Goku", "attributs": {"personnage": False, "homme": True, "anime": True, "film_serie": False, "acteur_chanteur": False, "historique": False, "dessin_anime": True, "jeu_video": True, "bande_dessinee": True, "litterature": False, "mythologie": False, "science_fiction": False, "fantasy": True, "comedie": False, "drame": False, "romance": False}},
    {"nom": "Sailor Moon", "attributs": {"personnage": False, "homme": False, "anime": True, "film_serie": False, "acteur_chanteur": False, "historique": False, "dessin_anime": True, "jeu_video": True, "bande_dessinee": True, "litterature": False, "mythologie": False, "science_fiction": False, "fantasy": True, "comedie": False, "drame": False, "romance": True}},

    # Personnages de films et séries
    {"nom": "Harry Potter", "attributs": {"personnage": False, "homme": True, "anime": False, "film_serie": True, "acteur_chanteur": False, "historique": False, "dessin_anime": False, "jeu_video": True, "bande_dessinee": False, "litterature": True, "mythologie": False, "science_fiction": False, "fantasy": True, "comedie": False, "drame": False, "romance": False}},
    {"nom": "Daenerys Targaryen", "attributs": {"personnage": False, "homme": False, "anime": False, "film_serie": True, "acteur_chanteur": False, "historique": False, "dessin_anime": False, "jeu_video": False, "bande_dessinee": False, "litterature": True, "mythologie": False, "science_fiction": False, "fantasy": True, "comedie": False, "drame": True, "romance": True}},
    {"nom": "Tony Stark", "attributs": {"personnage": False, "homme": True, "anime": False, "film_serie": True, "acteur_chanteur": False, "historique": False, "dessin_anime": False, "jeu_video": True, "bande_dessinee": True, "litterature": False, "mythologie": False, "science_fiction": True, "fantasy": False, "comedie": True, "drame": False, "romance": False}},
    {"nom": "Walter White", "attributs": {"personnage": False, "homme": True, "anime": False, "film_serie": True, "acteur_chanteur": False, "historique": False, "dessin_anime": False, "jeu_video": False, "bande_dessinee": False, "litterature": False, "mythologie": False, "science_fiction": False, "fantasy": False, "comedie": False, "drame": True, "romance": False}},
    {"nom": "Eleven", "attributs": {"personnage": False, "homme": False, "anime": False, "film_serie": True, "acteur_chanteur": False, "historique": False, "dessin_anime": False, "jeu_video": False, "bande_dessinee": False, "litterature": False, "mythologie": False, "science_fiction": True, "fantasy": False, "comedie": False, "drame": True, "romance": False}},

    # Acteurs ou chanteurs
    {"nom": "Brad Pitt", "attributs": {"personnage": True, "homme": True, "anime": False, "film_serie": False, "acteur_chanteur": True, "historique": False, "dessin_anime": False, "jeu_video": False, "bande_dessinee": False, "litterature": False, "mythologie": False, "science_fiction": False, "fantasy": False, "comedie": True, "drame": True, "romance": True}},
    {"nom": "Beyoncé", "attributs": {"personnage": True, "homme": False, "anime": False, "film_serie": False, "acteur_chanteur": True, "historique": False, "dessin_anime": False, "jeu_video": False, "bande_dessinee": False, "litterature": False, "mythologie": False, "science_fiction": False, "fantasy": False, "comedie": False, "drame": False, "romance": True}},
    {"nom": "Leonardo DiCaprio", "attributs": {"personnage": True, "homme": True, "anime": False, "film_serie": False, "acteur_chanteur": True, "historique": False, "dessin_anime": False, "jeu_video": False, "bande_dessinee": False, "litterature": False, "mythologie": False, "science_fiction": False, "fantasy": False, "comedie": True, "drame": True, "romance": True}},
    {"nom": "Adele", "attributs": {"personnage": True, "homme": False, "anime": False, "film_serie": False, "acteur_chanteur": True, "historique": False, "dessin_anime": False, "jeu_video": False, "bande_dessinee": False, "litterature": False, "mythologie": False, "science_fiction": False, "fantasy": False, "comedie": False, "drame": False, "romance": True}},
    {"nom": "Dwayne Johnson", "attributs": {"personnage": True, "homme": True, "anime": False, "film_serie": False, "acteur_chanteur": True, "historique": False, "dessin_anime": False, "jeu_video": False, "bande_dessinee": False, "litterature": False, "mythologie": False, "science_fiction": False, "fantasy": False, "comedie": True, "drame": True, "romance": False}}
]

# Liste des questions sur les animaux
question_animaux = [
    {"id": 1, "texte": "Est-ce un animal domestique ?", "attribut": "domestique"},
    {"id": 2, "texte": "Est-ce un mammifère ?", "attribut": "mammifere"},
    {"id": 3, "texte": "Est-ce un animal marin ?", "attribut": "marin"},
    {"id": 4, "texte": "Est-ce un animal volant ?", "attribut": "volant"},
    {"id": 5, "texte": "Est-ce un animal carnivore ?", "attribut": "carnivore"},
    {"id": 6, "texte": "Est-ce un animal herbivore ?", "attribut": "herbivore"},
    {"id": 7, "texte": "Est-ce un animal omnivore ?", "attribut": "omnivore"},
    {"id": 8, "texte": "Est-ce un animal nocturne ?", "attribut": "nocturne"},
    {"id": 9, "texte": "Est-ce un animal diurne ?", "attribut": "diurne"},
    {"id": 10, "texte": "Est-ce un animal sauvage ?", "attribut": "sauvage"},
    {"id": 11, "texte": "Est-ce un animal de compagnie ?", "attribut": "compagnie"},
    {"id": 12, "texte": "Est-ce un animal de ferme ?", "attribut": "ferme"},
    {"id": 13, "texte": "Est-ce un animal de zoo ?", "attribut": "zoo"},
    {"id": 14, "texte": "Est-ce un animal de forêt ?", "attribut": "foret"},
    {"id": 15, "texte": "Est-ce un animal de désert ?", "attribut": "desert"}
]

# Liste des animaux
animaux = [
    {"nom": "Chien", "attributs": {"domestique": True, "mammifere": True, "marin": False, "volant": False, "carnivore": True, "herbivore": False, "omnivore": True, "nocturne": False, "diurne": True, "sauvage": False, "compagnie": True, "ferme": False, "zoo": False, "foret": False, "desert": False}},
    {"nom": "Chat", "attributs": {"domestique": True, "mammifere": True, "marin": False, "volant": False, "carnivore": True, "herbivore": False, "omnivore": False, "nocturne": True, "diurne": True, "sauvage": False, "compagnie": True, "ferme": False, "zoo": False, "foret": False, "desert": False}},
    {"nom": "Dauphin", "attributs": {"domestique": False, "mammifere": True, "marin": True, "volant": False, "carnivore": True, "herbivore": False, "omnivore": False, "nocturne": False, "diurne": True, "sauvage": True, "compagnie": False, "ferme": False, "zoo": True, "foret": False, "desert": False}},
    {"nom": "Aigle", "attributs": {"domestique": False, "mammifere": False, "marin": False, "volant": True, "carnivore": True, "herbivore": False, "omnivore": False, "nocturne": False, "diurne": True, "sauvage": True, "compagnie": False, "ferme": False, "zoo": True, "foret": True, "desert": False}},
    {"nom": "Pigeon", "attributs": {"domestique": False, "mammifere": False, "marin": False, "volant": True, "carnivore": False, "herbivore": True, "omnivore": False, "nocturne": False, "diurne": True, "sauvage": True, "compagnie": False, "ferme": False, "zoo": False, "foret": False, "desert": False}},
    {"nom": "Lion", "attributs": {"domestique": False, "mammifere": True, "marin": False, "volant": False, "carnivore": True, "herbivore": False, "omnivore": False, "nocturne": True, "diurne": True, "sauvage": True, "compagnie": False, "ferme": False, "zoo": True, "foret": False, "desert": True}},
    {"nom": "Éléphant", "attributs": {"domestique": False, "mammifere": True, "marin": False, "volant": False, "carnivore": False, "herbivore": True, "omnivore": False, "nocturne": False, "diurne": True, "sauvage": True, "compagnie": False, "ferme": False, "zoo": True, "foret": True, "desert": False}},
    {"nom": "Koala", "attributs": {"domestique": False, "mammifere": True, "marin": False, "volant": False, "carnivore": False, "herbivore": True, "omnivore": False, "nocturne": True, "diurne": True, "sauvage": True, "compagnie": False, "ferme": False, "zoo": True, "foret": True, "desert": False}},
    {"nom": "Chauve-souris", "attributs": {"domestique": False, "mammifere": True, "marin": False, "volant": True, "carnivore": True, "herbivore": False, "omnivore": False, "nocturne": True, "diurne": False, "sauvage": True, "compagnie": False, "ferme": False, "zoo": False, "foret": True, "desert": False}},
    {"nom": "Crocodile", "attributs": {"domestique": False, "mammifere": False, "marin": True, "volant": False, "carnivore": True, "herbivore": False, "omnivore": False, "nocturne": True, "diurne": True, "sauvage": True, "compagnie": False, "ferme": False, "zoo": True, "foret": False, "desert": False}}
]


# Liste des questions sur les objets
question_objets = [
     {"id": 1, "texte": "Est-ce un objet technologique ?", "attribut": "technologique"},
    {"id": 2, "texte": "Est-ce un objet de cuisine ?", "attribut": "cuisine"},
    {"id": 3, "texte": "Est-ce un objet de décoration ?", "attribut": "decoration"},
    {"id": 4, "texte": "Est-ce un objet de sport ?", "attribut": "sport"},
    {"id": 5, "texte": "Est-ce un objet de bureau ?", "attribut": "bureau"},
    {"id": 6, "texte": "Est-ce un objet de jardinage ?", "attribut": "jardinage"},
    {"id": 7, "texte": "Est-ce un objet de musique ?", "attribut": "musique"},
    {"id": 8, "texte": "Est-ce un objet de transport ?", "attribut": "transport"},
    {"id": 9, "texte": "Est-ce un objet de loisir ?", "attribut": "loisir"},
    {"id": 10, "texte": "Est-ce un objet de sécurité ?", "attribut": "securite"},
    {"id": 11, "texte": "Est-ce un objet de bricolage ?", "attribut": "bricolage"},
    {"id": 12, "texte": "Est-ce un objet de camping ?", "attribut": "camping"},
    {"id": 13, "texte": "Est-ce un objet de fitness ?", "attribut": "fitness"},
    {"id": 14, "texte": "Est-ce un objet de jeu ?", "attribut": "jeu"},
    {"id": 15, "texte": "Est-ce un objet de travail ?", "attribut": "travail"}
]

# Liste des objets
objets = [
    {"nom": "Smartphone", "attributs": {"technologique": True, "cuisine": False, "decoration": False, "sport": False, "bureau": False, "jardinage": False, "musique": True, "transport": False, "loisir": True, "securite": False, "bricolage": False, "camping": False, "fitness": False, "jeu": True, "travail": True}},
    {"nom": "Table", "attributs": {"technologique": False, "cuisine": True, "decoration": False, "sport": False, "bureau": True, "jardinage": False, "musique": False, "transport": False, "loisir": False, "securite": False, "bricolage": False, "camping": False, "fitness": False, "jeu": False, "travail": True}},
    {"nom": "Vélo", "attributs": {"technologique": False, "cuisine": False, "decoration": False, "sport": True, "bureau": False, "jardinage": False, "musique": False, "transport": True, "loisir": True, "securite": False, "bricolage": False, "camping": False, "fitness": True, "jeu": False, "travail": False}},
    {"nom": "Lampe", "attributs": {"technologique": False, "cuisine": False, "decoration": True, "sport": False, "bureau": True, "jardinage": False, "musique": False, "transport": False, "loisir": False, "securite": False, "bricolage": False, "camping": False, "fitness": False, "jeu": False, "travail": False}},
    {"nom": "Télévision", "attributs": {"technologique": True, "cuisine": False, "decoration": False, "sport": False, "bureau": False, "jardinage": False, "musique": False, "transport": False, "loisir": True, "securite": False, "bricolage": False, "camping": False, "fitness": False, "jeu": True, "travail": False}},
    {"nom": "Ordinateur", "attributs": {"technologique": True, "cuisine": False, "decoration": False, "sport": False, "bureau": True, "jardinage": False, "musique": False, "transport": False, "loisir": True, "securite": False, "bricolage": False, "camping": False, "fitness": False, "jeu": True, "travail": True}},
    {"nom": "Casque", "attributs": {"technologique": True, "cuisine": False, "decoration": False, "sport": False, "bureau": False, "jardinage": False, "musique": True, "transport": False, "loisir": True, "securite": False, "bricolage": False, "camping": False, "fitness": False, "jeu": True, "travail": False}},
    {"nom": "Voiture", "attributs": {"technologique": True, "cuisine": False, "decoration": False, "sport": False, "bureau": False, "jardinage": False, "musique": False, "transport": True, "loisir": True, "securite": True, "bricolage": False, "camping": False, "fitness": False, "jeu": False, "travail": False}},
    {"nom": "Ballon", "attributs": {"technologique": False, "cuisine": False, "decoration": False, "sport": True, "bureau": False, "jardinage": False, "musique": False, "transport": False, "loisir": True, "securite": False, "bricolage": False, "camping": False, "fitness": True, "jeu": True, "travail": False}},
    {"nom": "Tondeuse", "attributs": {"technologique": False, "cuisine": False, "decoration": False, "sport": False, "bureau": False, "jardinage": True, "musique": False, "transport": False, "loisir": False, "securite": False, "bricolage": True, "camping": False, "fitness": False, "jeu": False, "travail": False}}
]
