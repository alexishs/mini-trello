import trello as tre

def demander_choix_menu(liste_choix: list)-> int:
    print("Faites un choix...")
    for numero_choix in range(len(liste_choix)):
        print(f"{numero_choix + 1} : {liste_choix[numero_choix]}")
    choix = int(input('Votre choix : ')) - 1
    return choix

def ouvrir_board(dictionnaire_trello):
    board_a_ouvrir = input("Nom du board à ouvrir : ")
    board = tre.board(board_a_ouvrir, dictionnaire_trello)
    print(board)