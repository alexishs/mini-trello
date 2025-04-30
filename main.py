import affichage as aff
import trello as tre

# def demander_choix_menu(liste_choix: list)-> int:
#     print("Faites un choix...")
#     for numero_choix in range(len(liste_choix)):
#         print(f"{numero_choix + 1} : {liste_choix[numero_choix]}")
#     choix = int(input('Votre choix : ')) - 1
#     return choix

# def ouvrir_board():
#     board_a_ouvrir = input("Nom du board à ouvrir : ")
#     board = trello.board(board_a_ouvrir)
#     print(board)

def main():
    
    tre.charger_fichier()
    #trello.supprimer_board('mon_premier_board')
    menu_principale = ["Lister les boards", "Afficher un board éxistant", "Quitter le programme"]
    choix = -1
    while choix != 2:
        choix = aff.demander_choix_menu(menu_principale)
        match choix:
            case 0:
                for nom_board in tre.liste_boards():
                    print(f"- {nom_board}")
            case 1:
                aff.ouvrir_board()

    tre.enregistrer_fichier()

main()