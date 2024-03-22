from film import Film
import json
import re


class Bibliotheque:
    def __init__(self, liste_films=[]):
        self.liste_films = liste_films

    def ajouter_film(self, film):
        self.liste_films.append(film)

    def afficher_films(self):
        return self.liste_films


    def mostrate(self):
        for f in self.liste_films:
            if f.note == max([film.get_note() for film in self.liste_films]):
                return f

    def top3(self):
        listeFilm = []
        for f in self.liste_films:
            if f.note == max([film.get_note() for film in self.liste_films]):
                listeFilm.append(f.get_titre())

        return listeFilm[:3]

    def lastmovie(self):
        date_pattern = re.compile(r"\d{4}-\d{2}-\d{2}")
        for f in self.liste_films:
            if f.date_sortie == max([film.get_date_sortie() for film in self.liste_films if date_pattern.match(film.get_date_sortie())]):
                return f

    def avrgnote(self):
        return sum([film.note for film in self.liste_films])/len(self.liste_films)

    def to_json_file(self, file):
        json_data = {
            "films": [film.to_json() for film in self.liste_films]
        }

        with open(file, "w") as file:
            json.dump(json_data, file)

        return json_data

    def fromjson(self, file):
        with open(file, "r") as file:
            data = json.load(file)
            for film in data["films"]:
                self.liste_films.append(Film(film["titre"], film["date"], film["note"], film["avis"]))
        return self.liste_films
