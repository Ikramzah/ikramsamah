# pylint: disable=C2401
"""
Ce module contient des classes d'exceptions personnalisées pour le projet.
"""
class ErreurDate(RuntimeError):
    """
    Exception levée pour les erreurs liées aux dates.
    """

class ErreurQuantité(RuntimeError):
    """
    Exception levée pour les erreurs liées aux quantités.
    """

class LiquiditéInsuffisante(RuntimeError):
    """
    Exception levée pour les erreurs de liquidité insuffisante.
    """
