import my_package_MT.find3 as find3
import find1
import find2

def menu():
    print("Menu:")
    print("1. Find1")
    print("2. Find2")
    print("3. Find3")
    print("4. Quitter")
    choix = input("Veuillez choisir une option (1-4): ")
    return choix


def start_menu():
    choix = menu()
    match choix:
        case "1":
            find1.start_find1()
        case "2":
            find2.start_find2()
        case "3":
            find3.start_find3()
        case "4":
            print("Au revoir!")
        case _:
            print("Choix invalide")
            start_menu()


if __name__ == '__main__':
    start_menu()