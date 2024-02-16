# Description: Copier le contenu d'un fichier dans un autre fichier en supprimant les lignes vides.

def fichier1():
    file = open('f_exercice2.txt', 'r')
    file2 = open('f1_exercice2.txt', 'w')
    for line in file:
        if line != "\n":
            file2.write(line)
    file.close()
    file2.close()



def fichier2():
    with open('f_exercice2.txt', 'r') as file:
        with open('f2_exercice2.txt', 'w') as file2:
            for line in file:
                if line != "\n":
                    file2.write(line)




if __name__ == '__main__':
    fichier1()
    fichier2()
    print("Les fichiers ont été copiés.")