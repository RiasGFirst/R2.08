import re


def lecture1(name):
    try:
        with open(name, "r") as fichier:
            return fichier.read()
    except FileNotFoundError:
        return f"Le fichier {name} n'a pas été trouvé."
    except PermissionError:
        return f"Vous n'avez pas la permission de lire le fichier {name}."
    except IOError:
        return f"Erreur lors de la lecture du fichier {name}."
    except OSError:
        return f"Erreur système lors de la lecture du fichier {name}."
    except Exception as e:
        return f"Erreur: {e}"

def lecture2(name, word):
    nb_word = 0
    with open(name, "r") as fichier:
        for line in fichier:
            nb_word += line.count(word)
            print(line)
        return f"Le mot {word} a été trouvé {nb_word} fois."


def lecture3(name):
    try:
        with open(name, "r") as fichier:
            for line in fichier:
                for word in line.split():
                    regex = re.compile("^([+-]?[0-9]+\.?[0-9]*)$")
                    if regex.match(word) is not None:
                        print("C’est un ???.")
                    else:
                        print("Ce n’est pas un ????.")
    except FileNotFoundError:
        return f"Le fichier {name} n'a pas été trouvé."
    except PermissionError:
        return f"Vous n'avez pas la permission de lire le fichier {name}."
    except IOError:
        return f"Erreur lors de la lecture du fichier {name}."
    except OSError:
        return f"Erreur système lors de la lecture du fichier {name}."


if __name__ == '__main__':
    print(lecture3('f_exercice3.txt'))
