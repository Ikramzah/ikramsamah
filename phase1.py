import argparse
import requests
import json
from datetime import datetime

def analyser_commande():
    parser = argparse.ArgumentParser(description="Extraction des valeurs historiques des titres boursiers")

    parser.add_argument("-s", metavar="symbole", dest="symbole", type=str, nargs="+", help="Nom d'un symbole boursier")
    parser.add_argument("-d", "--debut", dest="debut", type=str, help="Date recherchée la plus ancienne (format: AAAA-MM-JJ)")
    parser.add_argument("-f", "--fin", dest="fin", type=str, help="Date recherchée la plus récente (format: AAAA-MM-JJ)")
    parser.add_argument("-v", "--valeur", dest="valeur", choices=["fermeture", "ouverture", "min", "max", "volume"], default="fermeture", help="La valeur désirée (par défaut = fermeture)")

    args = parser.parse_args()
    print(args)  
    return args

def produire_historique(symbole, debut, fin, valeur):
    url = f'https://pax.ulaval.ca/action/{symbole}/historique/'

    params = {'debut': debut, 'fin': fin}

    response = requests.get(url=url, params=params)
    data = response.json().get('historique', {})

    historique = [(datetime.strptime(date_str, '%Y-%m-%d').date(), values[valeur]) for date_str, values in data.items()]

    print(f'titre={symbole}: valeur={valeur}, début={debut}, fin={fin}')
    print(historique)

if __name__ == "__main__":
    args = analyser_commande()
    if args.symbole is not None:
        for symbole in args.symbole:
            produire_historique(symbole, args.debut, args.fin, args.valeur)
    else:
        print("No symbole provided.")
