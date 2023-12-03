# pylint: disable=R0903
"""
Ce module contient la classe bourse
"""
from datetime import date
from phase1 import produire_historique
from exceptions import ErreurDate

class Bourse():
    """
    La classe Bourse représente un marché financier.
    """
    def __init__(self):
        pass

    def prix(self, symbole, date_interet):
        """
        Cette fonction retourne le prix de fermeture du symbole boursier à la date spécifiée
        """
        if date_interet > date.today():
          raise ErreurDate("La date d'interet ne peut pas etre dans le future.")

        historique = produire_historique(symbole, None, date_interet, 'fermeture')

        if historique:
            return historique[0][1]
        raise ErreurDate("Aucune donnee historique disponible avant la date specifiee.")


bourse1 = Bourse()
print(bourse1.prix('goog', date(2023, 12, 27)))
