"""
Ce script fournit une interface en ligne de commande pour extraire des valeurs historiques
de stocks pour un ou plusieurs symboles.
"""
import argparse
from datetime import date
import json
import requests
from requests.exceptions import RequestException


def analyser_commande():
    """
    Générer un interpréteur de commande.

    Returns:
        Un objet Namespace tel que retourné par parser.parse_args().
        Cet objet aura l'attribut «symboles» représentant la liste des
        symboles à traiter, et les attributs «début», «fin» et «valeur»
        associés aux arguments optionnels de la ligne de commande.
    """
    parser = argparse.ArgumentParser(
        description="Extraction de valeurs historiques pour un ou plusieurs symboles boursiers.")
    parser.add_argument("symboles",
                        nargs="+",
                        help="Nom d'un symbole boursier")
    parser.add_argument("-d", "--debut",
                        type=date.fromisoformat,
                        metavar='date de debut',
                        help="Date recherchée la plus ancienne (format: AAAA-MM-JJ)")
    parser.add_argument("-f", "--fin",
                        type=date.fromisoformat,
                        metavar='date de fin',
                        help="Date recherchée la plus récente (format: AAAA-MM-JJ)")
    parser.add_argument("-v", "--valeur",
                        metavar='valeur voulue',
                        choices=["fermeture", "ouverture", "min", "max", "volume"],
                        default="fermeture",
                        help="La valeur désirée (par défaut: fermeture)")

    return parser.parse_args()


def produire_historique(symbole, debut, fin, valeur):
    """
    Récupère les données historiques du symbole boursier pour la plage de dates spécifiée.

    Args:
        symbole (str): Symbole boursier.
        debut (date): Date de début.
        fin (date): Date de fin.
        valeur (str): Valeur souhaitée ('fermeture', 'ouverture', 'min', 'max', 'volume').

    Returns:
        list: Liste de tuples contenant la date et la valeur spécifiée pour le symbole boursier.
    Raises:
        RequestException: En cas d'erreur serveur.
    """
    url = f'https://pax.ulaval.ca/action/{symbole}/historique/'
    params = {
        'début': debut.isoformat() if debut else None,
        'fin': fin.isoformat() if fin else None,
    }
    try:
        response = requests.get(url=url, params=params, timeout=10)
        response.raise_for_status()
    except RequestException as req_error:
        raise RequestException(f'Erreur de requête: {req_error}') from req_error

    response_data = json.loads(response.text)
    if 'historique' in response_data:
        historique = response_data['historique']
        historique_filtre = [
        (date.fromisoformat(date_str), values[valeur]) for date_str, values in historique.items()]
        return historique_filtre
    raise RequestException('Erreur du serveur: Réponse inattendue', response_data)


def main():
    """
    Fonction principale pour exécuter le programme.
    """
    args = analyser_commande()
    for symbole in args.symboles:
        if args.fin:
            fin = args.fin
        else:
            fin = date.today()

        debut = args.debut if args.debut else fin

        historique = produire_historique(symbole, debut, fin, args.valeur)
        historique.sort(key=lambda x: x[0])

        debut_str = f"{debut:%Y-%m-%d}"
        fin_str = f"{fin:%Y-%m-%d}"

        print(
            f"titre={symbole}: valeur={args.valeur}, "
            f"début=datetime.date({date.fromisoformat(debut_str).year}, "
            f"{date.fromisoformat(debut_str).month}, {date.fromisoformat(debut_str).day}), "
            f"fin=datetime.date({date.fromisoformat(fin_str).year}, "
            f"{date.fromisoformat(fin_str).month}, {date.fromisoformat(fin_str).day})"
        )
        print(historique)

if __name__ == "__main__":
    main()
