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
        if quantité > 








     #l'achat de la quantité d'actions du titre symbole à la date spécifiée"