class Voiture:
    cpt_voiture = 0 

    def __init__(self,marque,modele,annee,litre_essence=100):

        self.marque = marque
        self.modele = modele
        self.annee = annee
        Voiture.cpt_voiture +=1
        self.litre_essence =litre_essence

    def afficher_detail(self):
        print (f"Marque : {self.marque}, modele : {self.modele}, annee : {self.annee}" )

    @classmethod
    def afficher_nombre_vehicule(cls):
        print (f"le nombre de véhicule est de : {Voiture.cpt_voiture}")

    def demarrage(self):
        print (f"la voiture {self.marque} modele {self.modele} demarre ")

    def arret(self):
        print (f"la voiture {self.marque} modele {self.modele} s'arrete ")

    
    def rouler(self,nombre_km):
        self.litre_essence =self.litre_essence-(5*nombre_km)/100
        print(f"la voiture {self.modele} a {self.litre_essence}litres d'essence" )

    def faire_le_plein(self):
        self.litre_essence =100

        

voiture1 = Voiture("Tesla", "Model S", 2023,100)
voiture2 = Voiture("BMW", "X5", 2020,150)

voiture1.afficher_detail()
voiture2.afficher_detail()

Voiture.afficher_nombre_vehicule()

voiture1.demarrage()

voiture2.rouler(100)
