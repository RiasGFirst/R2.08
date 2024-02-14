from voiture import Voiture

mycar1 = Voiture()
mycar2 = Voiture()
mycar3 = Voiture(marque="Lamborgini", model="Aventador", puissancefiscale=740)
mycar4 = Voiture(couleur="noir")

print(mycar1.__dict__)
print(mycar2.afficher())
print(mycar3.afficher())
print(mycar4.afficher())

#mycar1.set_attributs("bleu", "Peugeot", "208", 5)
mycar2.set_attributs(couleur="blanc")
print(mycar2)
mycar2.set_attributs()
print(mycar2)

print(mycar1.get_attributs())
print(mycar2.get_attributs())

print(mycar1)

mycar1.ajouter_option("climatisation")
mycar1.ajouter_option("toit ouvrant")

print(mycar1)

mycar1.supprimer_option("climatisation")

print(mycar1)
