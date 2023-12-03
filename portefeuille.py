<<<<<<< HEAD
import datetime
from ikramsamah.exceptions import ErreurDate, ErreurQuantité, LiquiditéInsuffisante

class Portefeuille:
    def __init__(self, bourse):
        self.bourse = bourse
        self.liquidites = 0
        self.transactions = []  # initiation

    def déposer(self, montant, date=None):
        if date is None:
            date = datetime.date.today()

        if date > datetime.date.today():
            raise ErreurDate("La date futur n'est pas autorisée pour un dépôt")

        self.liquidites += montant
        self.transactions.append((date, f"le dépôt de ${montant: .2f}"))

    def solde(self, date=None):
        date = date or datetime.date.today()
        return self.liquidites

    def acheter(self, symbole, quantité, date=None):
        date = date or datetime.date.today()
        prix_unitaire = self.bourse.prix(symbole, date)
        cout_total = prix_unitaire * quantité

        self._verifier_liquidites_suffisantes(cout_total)

        self.liquidites -= cout_total
        self.transactions.append((date, f"Achat de {quantité} actions de {symbole}"))

    def vendre(self, symbole, quantité, date=None):
        date = date or datetime.date.today()
        prix_unitaire = self.bourse.prix(symbole, date)
        gain_total = prix_unitaire * quantité

        self._verifier_quantite_suffisante(symbole, quantité, date)

        self.liquidites += gain_total
        self.transactions.append((date, f"Vente de {quantité} actions de {symbole}"))

    def valeur_totale(self, date=None):
        date = date or datetime.date.today()

        total_liquidites = self.liquidites
        total_titres = sum(self.bourse.prix(symbole, date) * self.get_quantite(symbole, date)
                           for symbole in self.get_symboles_titres(date))

        return total_liquidites + total_titres

    def valeur_des_titres(self, symboles, date=None):
        date = date or datetime.date.today()
        return sum(self.bourse.prix(symbole, date) * self.get_quantite(symbole, date) for symbole in symboles)

    def titres(self, date=None):
        date = date or datetime.date.today()
        return {symbole: self.get_quantite(symbole, date) for symbole in self.get_symboles_titres(date)}

    def valeur_projetee(self, date, rendement):
        # Logique pour projeter la valeur du portefeuille à une date future avec le rendement spécifié
        pass

    def get_quantite(self, symbole, date):
        # Méthode utilitaire pour obtenir la quantité d'actions d'un titre à une date spécifiée
        pass

    def _verifier_liquidites_suffisantes(self, montant):
        if montant > self.liquidites:
            raise LiquiditéInsuffisante("Liquidités insuffisantes pour effectuer cette transaction")

    def _verifier_quantite_suffisante(self, symbole, quantité, date):
        quantite_actuelle = self.get_quantite(symbole, date)
        if quantité > quantite_actuelle:
            raise ErreurQuantité(f"Quantité insuffisante de {symbole} à vendre")

    def get_symboles_titres(self, date):
        # Méthode utilitaire pour obtenir les symboles de tous les titres du portefeuille à une date spécifiée
        pass
=======
import datetime 



class Portefeuille:
    
    def __init__(self, bourse1): 
        self.bourse1 = bourse1

    def déposer(self, montant, date):
       date = date("La date de transaction:", self.year, self.day, self.month)
       montant = type(float) + ' ' + '$'
       return f"'dépot du montant', {montant}, 'le', {date}" 
    # effectue le dépôt du montant liquide dans le portefeuille à la date spécifiée
   
    def solde(self, date):
        date_devaluation = date(self.day)
        historique = {}
        return date_devaluation() 
    # le solde des liquidités du portefeuille à la date spécifiée

    def acheter(self, symbole, quantité, date):
        if quantité


    def vendre(symbole, quantité, date)








     #l'achat de la quantité d'actions du titre symbole à la date spécifiée"
>>>>>>> ec0b9eb2d81bd65eae60388297992b53038e7cc3
