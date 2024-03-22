from bibliotheque import Bibliotheque


def main():
    biblio = Bibliotheque()
    biblio.fromjson("movies.json")
    print(f"Voici la liste des films :")
    for f in biblio.afficher_films():
        print(f)
    print("=====================================")
    print(f"Le film le mieux noté est :\n{biblio.mostrate()}")
    print("=====================================")
    print(f"Les 3 films les mieux notés sont :")
    for f in biblio.top3():
        print(f)
    print("=====================================")
    print(f"Le dernier film sorti est :\n{biblio.lastmovie()}")
    print("=====================================")
    print(f"La moyenne des notes des films est de {biblio.avrgnote()}")
    print("=====================================")
    biblio.to_json_file(file="movies3.json")


if __name__ == "__main__":
    main()