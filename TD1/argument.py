import sys

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print(f"Pas assez d'arguments pour le script: {sys.argv[0]}")
        exit(-1)
    else:
        for i in range(len(sys.argv)):
            print("Argument", i, ":", sys.argv[i])
        print("=====")
        for elt in sys.argv:
            print(elt)