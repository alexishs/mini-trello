# Structure du fichier json
# { # dictionnaire de boards
#    "nom du board" : { # board
#        a_faire : [str,],
#        en_cours : [str,],
#        termine : [str,]
#    },
# }

## BOARD


def generer_erreur_si_board_inexistant(
    nom_board: str, dictionnaire_trello: dict
) -> None:
    """
    Fonction qui génère une erreur si le board n'existe pas.

    Args:
        nom_board (str): Nom du board à vérifier.
        dictionnaire_trello (dict): Dictionnaire contenant les boards.

    Returns:
        None
    """
    if not nom_board in dictionnaire_trello.keys():
        raise Exception(f'Le board "{nom_board}" n\'existe pas.')


def liste_boards(dictionnaire_trello: dict) -> tuple:
    """
    Fonction qui renvoie la liste des boards.

    Args:
        dictionnaire_trello (dict): Dictionnaire contenant les boards.

    Returns:
        tuple: Liste des noms de boards.
    """
    return tuple(dictionnaire_trello.keys())


def ajouter_board(nom_board: str, dictionnaire_trello: dict) -> dict:
    """
    Fonction qui ajoute un board au dictionnaire.

    Args:
        nom_board (str): Nom du board à ajouter.
        dictionnaire_trello (dict): Dictionnaire contenant les boards.

    Returns:
        dict: Dictionnaire contenant le nouveau board.
    """
    # if nom_board in dictionnaire_trello.keys():
    if nom_board in list(dictionnaire_trello.keys()):
        raise Exception(f'Le board "{nom_board}" éxiste déjà. Ajout impossible.')
    nouveau_board = {"a_faire": [], "en_cours": [], "termine": []}
    dictionnaire_trello[nom_board] = nouveau_board
    return nouveau_board


def board(nom_board: str, dictionnaire_trello: dict) -> dict:
    """
    Fonction qui renvoie le board correspondant au nom donné.

    Args:
        nom_board (str): Nom du board à récupérer.
        dictionnaire_trello (dict): Dictionnaire contenant les boards.

    Returns:
        dict: Dictionnaire contenant le board demandé.
    """
    generer_erreur_si_board_inexistant(nom_board, dictionnaire_trello)
    return dictionnaire_trello[nom_board]


def supprimer_board(nom_board: str, dictionnaire_trello: dict) -> None:
    """
    Fonction qui supprime un board du dictionnaire.

    Args:
        nom_board (str): Nom du board à supprimer.
        dictionnaire_trello (dict): Dictionnaire contenant les boards.

    Returns:
        None
    """
    generer_erreur_si_board_inexistant(nom_board, dictionnaire_trello)
    del dictionnaire_trello[nom_board]


## TACHES (= cards)


def supprimer_tache(
    dictionnaire_trello: dict, nom_board: str, nom_colonne: str, libelle_tache: str
) -> None:
    """
    Fonction qui supprime une tâche du board.

    Args:
        dictionnaire_trello (dict): Dictionnaire contenant les boards.
        nom_board (str): Nom du board à supprimer.
        nom_colonne (str): Nom de la colonne à supprimer.
        libelle_tache (str): Libellé de la tâche à supprimer.

    Returns:
        None
    """
    generer_erreur_si_colonne_inexistante(nom_colonne)
    board(nom_board, dictionnaire_trello)[nom_colonne].remove(libelle_tache)


def generer_erreur_si_colonne_inexistante(nom_colonne: str) -> None:
    """
    Fonction qui génère une erreur si la colonne n'existe pas.

    Args:
        nom_colonne (str): Nom de la colonne à vérifier.

    Returns:
        None
    """
    if not nom_colonne in ("a_faire", "en_cours", "termine"):
        raise Exception(f'La colonne "{nom_colonne}" n\'existe pas.')


def ajouter_tache(
    dictionnaire_trello: dict, nom_board: str, nom_colonne: str, libelle_tache: str
) -> None:
    """
    Fonction qui ajoute une tâche au board.

    Args:
        dictionnaire_trello (dict): Dictionnaire contenant les boards.
        nom_board (str): Nom du board à ajouter.
        nom_colonne (str): Nom de la colonne à ajouter.
        libelle_tache (str): Libellé de la tâche à ajouter.

    Returns:
        None
    """
    generer_erreur_si_colonne_inexistante(nom_colonne)
    board_taches = board(nom_board, dictionnaire_trello)
    liste_taches = board_taches[nom_colonne]
    liste_taches.append(libelle_tache)


def deplacer_tache(
    dictionnaire_trello: dict,
    nom_board: str,
    nom_colonne_origine: str,
    nom_colonne_destination: str,
    libelle_tache: str,
) -> None:
    """
    Fonction qui déplace une tâche d'une colonne à une autre.

    Args:
        dictionnaire_trello (dict): Dictionnaire contenant les boards.
        nom_board (str): Nom du board à déplacer.
        nom_colonne_origine (str): Nom de la colonne d'origine.
        nom_colonne_destination (str): Nom de la colonne de destination.
        libelle_tache (str): Libellé de la tâche à déplacer.

    Returns:
        None
    """
    supprimer_tache(dictionnaire_trello, nom_board, nom_colonne_origine, libelle_tache)
    ajouter_tache(
        dictionnaire_trello, nom_board, nom_colonne_destination, libelle_tache
    )


def liste_taches(dictionnaire_trello: dict, nom_board: str, nom_colonne: str) -> list:
    """
    Fonction qui renvoie la liste des tâches d'une colonne.

    Args:
        dictionnaire_trello (dict): Dictionnaire contenant les boards.
        nom_board (str): Nom du board à lister.
        nom_colonne (str): Nom de la colonne à lister.

    Returns:
        list: Liste des tâches de la colonne.
    """
    board_liste_tache = board(nom_board, dictionnaire_trello)
    generer_erreur_si_colonne_inexistante(nom_colonne, dictionnaire_trello)
    return board_liste_tache[nom_colonne]
