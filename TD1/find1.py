import sys
import os


def affiche(dossier):
    content = os.listdir(dossier)
    for element in content:
        if os.path.isdir(element):
            print(f"{element}/")
        else:
            print(element)


def aide():
    print(f"Usage: {sys.argv[0]} <dossier>")
    print(f"Affiche le contenu du dossier <dossier>")
    exit(-1)


def start_find1():
    if len(sys.argv) <= 1:
        aide()
    else:
        if os.path.exists(sys.argv[1]):
            if os.path.isdir(sys.argv[1]):
                affiche(sys.argv[1])
            else:
                aide()
        else:
            aide()


if __name__ == '__main__':
    start_find1()
