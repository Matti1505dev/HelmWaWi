from ShoppingCart.shoppingCart import ShoppingCart  # Importiert die Einkaufswagen-Klasse.

class User():
    """
    Diese Klasse erstellt einen Benutzer mit persönlichen Daten und einem Einkaufswagen.
    """

    def __init__(self, email, name, password, adresse, tel):
        """
        Diese Funktion wird aufgerufen, wenn ein neuer Benutzer erstellt wird.
        Sie speichert die Benutzerdaten und gibt ihm einen Einkaufswagen.
        """
        self.shoppingCart = ShoppingCart()  # Jeder Benutzer bekommt seinen eigenen Einkaufswagen.
        self.email = email  # E-Mail-Adresse des Benutzers.
        self.name = name  # Name des Benutzers.
        self.password = password  # Passwort für das Benutzerkonto.
        self.adresse = adresse  # Wohnadresse des Benutzers.
        self.tel = tel  # Telefonnummer des Benutzers.
