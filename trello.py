    #Structure du fichier json
    #{ # dictionnaire de boards
    #    "nom du board" : { # board
    #        a_faire : [str,],
    #        en_cours : [str,],
    #        termine : [str,]
    #    },
    #}


def generer_erreur_si_board_inexistant(nom_board: str, dictionnaire_trello)-> None:
    if not nom_board in dictionnaire_trello.keys():
        raise Exception(f'Le board "{nom_board}" n\'éxiste pas.')

def liste_boards(dictionnaire_trello)->tuple:
    return tuple(dictionnaire_trello.keys())

def ajouter_board(nom_board: str, dictionnaire_trello)-> dict:
    #if nom_board in dictionnaire_trello.keys():
    if nom_board in list(dictionnaire_trello.keys()):
        raise Exception(f'Le board "{nom_board}" éxiste déjà. Ajout impossible.')
    nouveau_board = {
        "a_faire": [],
        "en_cours": [],
        "termine": []
    }
    dictionnaire_trello[nom_board] = nouveau_board
    return nouveau_board

def board(nom_board: str, dictionnaire_trello)-> dict:
    generer_erreur_si_board_inexistant(nom_board, dictionnaire_trello)
    return dictionnaire_trello[nom_board]

def supprimer_board(nom_board: str, dictionnaire_trello)-> None:
    generer_erreur_si_board_inexistant(nom_board, dictionnaire_trello)
    del(dictionnaire_trello[nom_board])

def generer_erreur_si_colonne_inexistante(nom_colonne)
    pass # développé par Romain

def supprimer_tache(dictionnaire_trello: dict, nom_board: str, nom_colonne: str, libelle_tache: str)-> None:
    generer_erreur_si_colonne_inexistante(nom_colonne)
    board(nom_board, dictionnaire_trello)[nom_colonne].remove(libelle_tache)