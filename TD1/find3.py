import sys
import os


def recherche(dossier, fichier, listeFinded, listeDossiers):
    for element in os.listdir(dossier):
        if os.path.isdir(f"{dossier}/{element}"):
            listeDossiers.append(f"{dossier}/{element}")
        else:
            if element == fichier:
                listeFinded.append(f"{dossier}/{element}")
    return listeFinded, listeDossiers


def affiche(listeFichiers):
    for element in listeFichiers:
        print(element)


def aide():
    print(f"Usage: {sys.argv[0]} <dossier> <fichier>")
    print(f"Cherche le fichier <fichier> dans le dossier <dossier> et ses sous-dossiers")
    exit(-1)


if __name__ == '__main__':
    if len(sys.argv) <= 2:
        aide()
    listeFinded = []
    listeDossiers = []
    fichiers, dossiers = recherche(sys.argv[1], sys.argv[2], listeFinded, listeDossiers)
    if len(dossiers) > 0:
        for dossier in dossiers:
            fichiers, dossiers = recherche(f"{dossier}", sys.argv[2], fichiers, dossiers)

    affiche(fichiers)
