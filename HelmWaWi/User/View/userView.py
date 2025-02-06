from User.Controller.userController import createUser  # Importiert die Funktion, um einen Benutzer zu erstellen.

def getUserData():
    """
    Diese Funktion fragt den Benutzer nach seinen Daten und erstellt ein neues Benutzerkonto.
    """

    # Der Benutzer gibt seine Informationen ein.
    email = input("Deine Email: ")  # E-Mail-Adresse des Benutzers.
    name = input("Dein Name: ")  # Name des Benutzers.
    password = input("Dein Passwort: ")  # Passwort für das Konto.
    adresse = input("Deine Adresse: ")  # Wohnadresse des Benutzers.
    tel = input("Deine Telefonnummer: ")  # Telefonnummer des Benutzers.

    # Die eingegebenen Daten werden genutzt, um den Benutzer zu erstellen und zu speichern.
    createUser(email, name, password, adresse, tel)
