class shoppingCart():
    """
    Diese Klasse stellt einen Einkaufswagen dar.
    Hier können verschiedene Artikel (Helme) gespeichert werden.
    """

    def __init__(self):
        """
        Diese Funktion wird aufgerufen, wenn ein neuer Einkaufswagen erstellt wird.
        Der Einkaufswagen startet mit einer leeren Artikelliste.
        """
        self.articel = []  # Eine Liste, in der die Artikel gespeichert werden.
