import json

def charger_fichier()-> None:
    with open('trello.json') as fichier:
        return json.load(fichier)

def enregistrer_fichier(dictionnaire_trello)-> None:
    with open('trello.json', 'w') as fichier:
        fichier.write(json.dumps(dictionnaire_trello))