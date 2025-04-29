import json

    #Structure du fichier json
    #{ # dictionnaire de boards
    #    "nom du board" : { # board
    #        a_faire : [str,],
    #        en_cours : [str,],
    #        termine : [str,]
    #    },
    #}

dictionnaire_trello = {}

def charger_fichier()-> None:
    global dictionnaire_trello
    with open('trello.json') as fichier:
        dictionnaire_trello = json.load(fichier)

def enregistrer_fichier()-> None:
    global dictionnaire_trello
    with open('trello.json', 'w') as fichier:
        fichier.write(json.dumps(dictionnaire_trello))

def generer_erreur_si_board_inexistant(nom_board: str)-> None:
    global dictionnaire_trello
    if not nom_board in dictionnaire_trello.keys():
        raise Exception(f'Le board "{nom_board}" n\'éxiste pas.')

def liste_boards()->tuple:
    global dictionnaire_trello
    return tuple(dictionnaire_trello.keys())

def ajouter_board(nom_board: str)-> dict:
    global dictionnaire_trello
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

def board(nom_board: str)-> dict:
    global dictionnaire_trello
    generer_erreur_si_board_inexistant(nom_board)
    return dictionnaire_trello[nom_board]

def supprimer_board(nom_board: str)-> None:
    global dictionnaire_trello
    generer_erreur_si_board_inexistant(nom_board)
    del(dictionnaire_trello[nom_board])