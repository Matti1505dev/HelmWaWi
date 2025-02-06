from Controller import Logic  # Importiert das Logik-Modul, das die Helm-Auswahl verarbeitet.
from Model import Helm  # Importiert das Helm-Modul, das die Helm-Daten enthält.

def getInput():
    """
    Diese Funktion fragt den Benutzer nach seinen Helm-Wünschen und speichert die Auswahl.
    Die eingegebenen Werte werden in die Logik (Logic.py) übertragen.
    """
    
    # Der Benutzer wählt eine Helmkategorie aus.
    kategorieAuswahl = input(f"Wähle bitte eine Helmkategorie. Zur Auswahl stehen:\n{Logic.HelmKategorien}")
    Logic.kategorie = Helm.HelmKategorien[int(kategorieAuswahl)]  # Die Eingabe wird in eine Kategorie umgewandelt.
    
    # Der Benutzer wählt eine Helmgröße aus.
    groesseAuswahl = input(f"Wähle bitte eine Helmgröße. Zur Auswahl stehen:\n{Logic.HelmSize}")
    Logic.groesse = Helm.HelmSize[int(groesseAuswahl)]
    
    # Der Benutzer wählt ein Helmmaterial aus.
    materialAuswahl = input(f"Wähle bitte ein Helmmaterial. Zur Auswahl stehen:\n{Logic.HelmMaterial}")
    Logic.material = Helm.HelmMaterial[int(materialAuswahl)]
    
    # Der Benutzer wählt eine Verschlussart aus.
    verschlussAuswahl = input(f"Wähle bitte einen Helmverschluss. Zur Auswahl stehen:\n{Logic.HelmLock}")
    Logic.verschluss = Helm.HelmVerschluss[int(verschlussAuswahl)]
    
    # Der Benutzer gibt einen maximalen Preis für den Helm ein.
    Logic.preis = int(input(f"Wähle bitte einen Maximalpreis.\n"))


def printHelmet():
    """
    Diese Funktion gibt die passenden Helme aus, die zur Auswahl des Benutzers passen.
    Die gefundenen Helme werden aus der Logik (Logic.py) genommen.
    """
    
    # Die Liste der gefundenen Helme wird in eine lesbare Zeichenkette umgewandelt.
    Logic.extractedHelmets = ", ".join(Logic.ConfirmedHelmet)
    
    # Die passenden Helme werden ausgegeben.
    print(f"Diese Helme: {Logic.extractedHelmets} stehen zur Auswahl")
