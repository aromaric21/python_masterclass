# Création de la classe Compte
class Compte:
    def __init__(self, solde):
        self.solde = solde

    def deposer(self, montant):
        if montant > 0:
            self.solde += montant
            print("Dépôt :", montant)
        else:
            print("Montant invalide")

    def retirer(self, montant):
       if montant <= 0:
            print("Montant invalide")
       elif  self.solde < montant:
            print("Solde inssufisant")
       else:
           self.solde -= montant
           print("Retrait : ", montant)

    def afficher(self):
        print("Solde :", self.solde)


solde = float(input("Solde initial :"))
c = Compte(solde)

while True:
    print("\n1.Dépôt 2.Retrait 3.Solde 4.Quitter")
    choix = int(input(">"))
    try:
        if choix == 1:
            montant = float(input("Montant:"))
            c.deposer(montant)
        elif choix == 2:
            montant = float(input("Montant:"))
            c.retirer(montant)
        elif choix == 3:
            c.afficher()
        elif choix == 4:
            break
        else:
            print("Choix invalide")
    except ValueError:
        print(" Entrer un nombre valide")