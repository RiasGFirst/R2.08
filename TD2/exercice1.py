

def divise1(a, b):
    return a / b


def divise2(a, b):
    if b == 0:
        return f"Erreur, b est égal à 0. Impossible de diviser par 0.\nLa division n'est donc pas possible."
    else:
        return a / b


def divise3(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return f"Erreur, b est égal à 0. Impossible de diviser par 0.\nLa division n'est donc pas possible."


if __name__ == '__main__':
    err = True
    while err:
        try:
            num1 = float(input("Entrez un nombre: "))
            num2 = float(input("Entrez un autre nombre: "))
            err = False
        except ValueError:
            print("Erreur, veuillez entrer un nombre.")
        except Exception as e:
            print(f"Erreur: {e}")
        else:
            div1 = divise3(num1, num2)
            print(f"La division de {num1} par {num2} est égale à {div1}")


