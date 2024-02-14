

class Voiture:
    def __init__(self, couleur="rouge", marque="Renault", model="Clio", puissancefiscale=4):
        self._couleur = couleur
        self._marque = marque
        self._modele = model
        self._puissancefiscale = puissancefiscale
        self._options = []

    def __str__(self):
        return f"""Voici les caractéristiques de cette voiture:
    - Marque: {self._marque}
    - Modèle: {self._modele}
    - Couleur: {self._couleur}
    - Puissance: {self._puissancefiscale}
    - Options: {self._options}
        """

    def get_attributs(self):
        return self._couleur, self._marque, self._modele, self._puissancefiscale, self._options

    def set_attributs(self, couleur=None, marque=None, model=None, puissancefiscale=None, options=[]):
        if couleur is not None:
            self._couleur = couleur
        if marque is not None:
            self._marque = marque
        if model is not None:
            self._modele = model
        if puissancefiscale is not None:
            self._puissancefiscale = puissancefiscale
        if options:
            for option in options:
                self._options.append(option)

    def ajouter_option(self, option):
        self._options.append(option)

    def supprimer_option(self, option):
        self._options.remove(option)

    def is_option_present(self, option):
        return option in self._options

    def afficher(self):
        return f"La voiture est de couleur {self._couleur}, de marque {self._marque}, de modèle {self._modele} et de puissance fiscale {self._puissancefiscale}"