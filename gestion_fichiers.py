import json
import os


def charger_fichier() -> None:
    """
    Fonction qui charge le fichier trello.json et le renvoie sous forme de dictionnaire.
    Si le fichier n'existe pas, il est créé avec un dictionnaire vide.

    Args:
        None

    Returns:
        dict: Dictionnaire contenant les données du fichier trello.json.
    """
    # on vérifie que le fichier trello.json existe dans le dossier
    if not os.path.exists("trello.json"):
        with open("trello.json", "w") as fichier:
            json.dump({}, fichier)

    with open("trello.json") as fichier:
        return json.load(fichier)


def enregistrer_fichier(dictionnaire_trello: dict) -> None:
    """
    Fonction qui enregistre le dictionnaire dans le fichier trello.json.

    Args:
        dictionnaire_trello (dict): Dictionnaire à enregistrer.

    Returns:
        None
    """
    with open("trello.json", "w") as fichier:
        fichier.write(json.dumps(dictionnaire_trello))
