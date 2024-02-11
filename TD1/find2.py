import sys
import os

def recherche(dossier, listeFichiers=[], listeDossiers=[]):
    for element in os.listdir(dossier):
        if os.path.isdir(f"{dossier}/{element}"):
            listeDossiers.append(f"{dossier}/{element}")
        else:
            listeFichiers.append(f"{dossier}/{element}")
    return listeFichiers, listeDossiers


def affiche(listeFichiers, listeDossiers):
    print(f"Contenu du dossier {sys.argv[1]}:")
    for element in listeDossiers:
        print(f"{element}/")
    for element in listeFichiers:
        print(element)


def aide():
    print(f"Usage: {sys.argv[0]} <dossier>")
    print(f"Affiche le contenu du dossier <dossier>")
    exit(-1)


def start_find2():
    if len(sys.argv) <= 1:
        aide()
    else:
        listeFichiers = []
        listeDossiers = []
        if os.path.isdir(sys.argv[1]):
            fichiers, dossiers = recherche(sys.argv[1], listeFichiers, listeDossiers)
            if len(dossiers) > 0:
                for dossier in dossiers:
                    fichiers, dossiers = recherche(f"{dossier}", fichiers, dossiers)
            affiche(fichiers, dossiers)
        else:
            aide()


if __name__ == '__main__':
    start_find2()