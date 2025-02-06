from User.Model.user import user  # Wir importieren die Benutzer-Klasse aus dem Benutzer-Modul.


def createUser(email, name, password, adresse, tel):
    """
    Diese Funktion erstellt einen neuen Benutzer und speichert ihn in einer Datei.
    """

    # Ein neues Benutzer-Objekt wird mit den eingegebenen Daten erstellt.
    createdUser = user(email, name, password, adresse, tel)

    # Die Benutzerdaten werden in einer Datei gespeichert.
    createdUser.speichern()
