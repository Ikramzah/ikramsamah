import datetime
from bourse import Bourse
from exceptions import ErreurDate, ErreurQuantité, LiquiditéInsuffisante

class Portefeuille:
    def __init__(self, bourse):   #initiation
        self.bourse = bourse
        self.transactions = []  
        self.solde_liquide = 0
        self.positions = {}

    def deposer(self, montant, date=None):  #dépot des liquidités
        if date is None:
            date = datetime.date.today()

        if date > datetime.date.today():
            raise ErreurDate("La date de dépôt ne peut pas être future.")

        self.solde_liquide += montant
        self.transactions.append((date, 'DEPOT', montant))

    def solde(self, date=None):  
        if date is None:
            date = datetime.date.today()

        if date > datetime.date.today():
            raise ErreurDate("La date d'évaluation ne peut pas être future.")

        solde = self.solde_liquide
        for transaction_date, transaction_type, montant in self.transactions:
            if transaction_date <= date:
                if transaction_type == 'ACHAT':
                    symbole = montant[0]
                    prix = self.bourse.prix(symbole, transaction_date)
                    solde -= prix * montant[1]  
                elif transaction_type == 'VENTE':
                    symbole = montant[0]
                    prix = self.bourse.prix(symbole, transaction_date)
                    solde += prix * montant[1]  

        return solde

    def acheter(self, symbole, quantite, date=None):
        if date is None:
            date = datetime.date.today()

        if date > datetime.date.today():
            raise ErreurDate("La date d'achat ne peut pas être future.")

        prix = self.bourse.prix(symbole, date)
        cout_total = prix * quantite

        if cout_total > self.solde_liquide:
            raise LiquiditéInsuffisante("Solde liquide insuffisant pour acheter ces actions.")

        self.solde_liquide -= cout_total
        if symbole in self.positions:
            self.positions[symbole] += quantite
        else:
            self.positions[symbole] = quantite

        self.transactions.append((date, 'ACHAT', (symbole, quantite)))

    def vendre(self, symbole, quantite, date=None):
        if date is None:
            date = datetime.date.today()

        if date > datetime.date.today():
            raise ErreurDate("La date de vente ne peut pas être future.")

        if symbole not in self.positions or self.positions[symbole] < quantite:
            raise ErreurQuantité(f"Quantité insuffisante de {symbole} pour la vente.")

        prix = self.bourse.prix(symbole, date)
        produit_total = prix * quantite

        self.solde_liquide += produit_total
        self.positions[symbole] -= quantite

        self.transactions.append((date, 'VENTE', (symbole, quantite)))

    def valeur_totale(self, date=None):
        if date is None:
            date = datetime.date.today()

        if date > datetime.date.today():
            raise ErreurDate("La date d'évaluation ne peut pas être future.")

        total = self.solde(date)
        for symbole, quantite in self.positions.items():
            prix = self.bourse.prix(symbole, date)
            total += prix * quantite

        return total

    def valeur_des_titres(self, symboles, date=None):
        if date is None:
            date = datetime.date.today()

        if date > datetime.date.today():
            raise ErreurDate("La date d'évaluation ne peut pas être future.")

        total = 0
        for symbole in symboles:
            if symbole in self.positions:
                prix = self.bourse.prix(symbole, date)
                total += prix * self.positions[symbole]

        return total

    def titres(self, date=None):
        if date is None:
            date = datetime.date.today()

        if date > datetime.date.today():
            raise ErreurDate("La date d'évaluation ne peut pas être future.")

        titres = {}
        for symbole, quantite in self.positions.items():
            if quantite > 0:
                titres[symbole] = quantite

        return titres

    def valeur_projetee(self, date, rendement):
        if date <= datetime.date.today():
            raise ErreurDate("La date projetée doit être future.")

        valeur_projetee = self.valeur_totale()
        for symbole, quantite in self.positions.items():
            rendement_titre = rendement.get(symbole, 0)
            prix = self.bourse.prix(symbole, date)
            valeur_projetee += quantite * prix * (1 + rendement_titre / 100) ** (date.year - datetime.date.today().year)

        return valeur_projetee
