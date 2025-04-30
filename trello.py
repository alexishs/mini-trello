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
    if not nom_board in dictionnaire_trello.keys():
        raise Exception(f'Le board "{nom_board}" n\'existe pas.')


def liste_boards(dictionnaire_trello: dict) -> tuple:
    return tuple(dictionnaire_trello.keys())


def ajouter_board(nom_board: str, dictionnaire_trello: dict) -> dict:
    # if nom_board in dictionnaire_trello.keys():
    if nom_board in list(dictionnaire_trello.keys()):
        raise Exception(f'Le board "{nom_board}" éxiste déjà. Ajout impossible.')
    nouveau_board = {"a_faire": [], "en_cours": [], "termine": []}
    dictionnaire_trello[nom_board] = nouveau_board
    return nouveau_board


def board(nom_board: str, dictionnaire_trello: dict) -> dict:
    generer_erreur_si_board_inexistant(nom_board, dictionnaire_trello)
    return dictionnaire_trello[nom_board]


def supprimer_board(nom_board: str, dictionnaire_trello: dict) -> None:
    generer_erreur_si_board_inexistant(nom_board, dictionnaire_trello)
    del dictionnaire_trello[nom_board]


## TACHES (= cards)


def supprimer_tache(
    dictionnaire_trello: dict, nom_board: str, nom_colonne: str, libelle_tache: str
) -> None:
    generer_erreur_si_colonne_inexistante(nom_colonne)
    board(nom_board, dictionnaire_trello)[nom_colonne].remove(libelle_tache)


def generer_erreur_si_colonne_inexistante(nom_colonne: str) -> None:
    if not nom_colonne in ("a_faire", "en_cours", "termine"):
        raise Exception(f'La colonne "{nom_colonne}" n\'existe pas.')


def ajouter_tache(
    dictionnaire_trello: dict, nom_board: str, nom_colonne: str, libelle_tache: str
) -> None:

    generer_erreur_si_colonne_inexistante(nom_colonne)
    board_taches = board(nom_board, dictionnaire_trello)
    liste_taches = board_taches[nom_colonne]
    liste_taches.append(libelle_tache)

def deplacer_tache(dictionnaire_trello: dict, nom_board: str, nom_colonne_origine: str, nom_colonne_destination: str, libelle_tache: str)-> None:
    supprimer_tache(dictionnaire_trello, nom_board, nom_colonne_origine, libelle_tache)
    ajouter_tache(dictionnaire_trello, nom_board, nom_colonne_destination, libelle_tache)

def liste_taches(dictionnaire_trello: dict, nom_board: str, nom_colonne: str)-> None:
    pass