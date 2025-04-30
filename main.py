import affichage as aff
import trello as tre
import gestion_fichiers as gf


def main():
    dictionnaire_trello = gf.charger_fichier()
    # trello.supprimer_board('mon_premier_board')
    menu_principale = [
        "Lister les boards",
        "Afficher un board éxistant",
        "Quitter le programme",
    ]
    choix = -1
    while choix != 2:
        choix = aff.demander_choix_menu(menu_principale)
        match choix:
            case 0:
                for nom_board in tre.liste_boards(dictionnaire_trello):
                    print(f"- {nom_board}")
            case 1:
                aff.ouvrir_board(dictionnaire_trello)

    gf.enregistrer_fichier(dictionnaire_trello)


main()
