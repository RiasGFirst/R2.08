import json


class Film:

    def __init__(self, titre, date_sortie, note, avis):
        self.__titre = titre
        self.__date_sortie = date_sortie
        self.__note = note
        self.__avis = avis

    def __str__(self):
        avis = ""
        for i in self.get_avis():
            avis += f"- {i}\n"

        return f"""
        le film {self.get_titre()} est sortie le {self.get_date_sortie()}, il a la note {self.get_note()} et
        voici les avis du public l'ayant vu :
        {avis}
        """

    def get_titre(self):
        return self.__titre

    def get_date_sortie(self):
        return self.__date_sortie

    def get_note(self):
        return self.__note

    def get_avis(self):
        return self.__avis

    titre = property(fget=get_titre)
    date_sortie = property(fget=get_date_sortie)
    note = property(fget=get_note)
    avis = property(fget=get_avis)

    def to_json(self):
        json_data = {
            "titre": self.get_titre(),
            "date_sortie": self.get_date_sortie(),
            "note": self.get_note(),
            "avis": self.get_avis()
        }

        return json_data
