import trello as tre

def demander_choix_menu(liste_choix: list)-> int:
    while True:
        print("Faites un choix...")
        for numero_choix in range(len(liste_choix)):
            print(f"{numero_choix + 1} : {liste_choix[numero_choix]}")
        choix = input('Votre choix : ')
        if choix.isnumeric():
            valeur_numerique = int(choix)
            if 1 <= valeur_numerique <= (len(liste_choix) + 1):
                return valeur_numerique - 1
        print("Numéro non reconnu.")

def choisir_colonne()-> str:
    print("Choisissez la colonne :")
    numero_choix = demander_choix_menu(("A faire", "En cours", "Terminés"))
    match numero_choix:
        case 0: return 'a_faire' 
        case 1: return 'en_cours' 
        case 2: return 'termine' 

def choisir_libelle_tache()-> str:
    return input('Saisissez un libellé de tache : ')

def ouvrir_board(dictionnaire_trello: dict):
    nom_board_choisi = input("Nom du board à ouvrir : ")
    print(f"debug : board ouvert : {tre.board(nom_board_choisi, dictionnaire_trello)}")
    choix = -1
    while choix != 4:
        choix = demander_choix_menu(("Ajouter une tache", "Déplacer tache", "Supprimer tache", "Lister les taches", "Revenir au menu principal"))
        match choix:
            case 0:
                nom_colonne = choisir_colonne()
                libelle_tache = choisir_libelle_tache()
                tre.ajouter_tache(dictionnaire_trello, nom_board_choisi, nom_colonne, libelle_tache)
            case 1:
                print("Colonne d'orifine")
                nom_colonne_origine = choisir_colonne()
                print("Colonne de destinaton")
                nom_colonne_destination = choisir_colonne()
                libelle_tache = choisir_libelle_tache()
                tre.deplacer_tache(dictionnaire_trello, nom_board_choisi, nom_colonne_origine, nom_colonne_destination, libelle_tache)
            case 2:
                nom_colonne = choisir_colonne()
                libelle_tache = choisir_libelle_tache()
                tre.supprimer_tache(dictionnaire_trello, nom_board_choisi, nom_colonne, libelle_tache)
            case 3:
                nom_colonne = choisir_colonne()
                print(tre.liste_taches(dictionnaire_trello, nom_board_choisi, nom_colonne))