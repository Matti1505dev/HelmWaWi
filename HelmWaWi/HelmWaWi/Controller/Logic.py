# Wir importieren zwei Module aus dem Model-Ordner:
from Model import Helm  # Das Helm-Modul enthält verschiedene Helmeigenschaften.
from Model import HelmBestand  # Das HelmBestand-Modul enthält eine Liste aller Helme.

# Variablen für die Eigenschaften eines Helms
groesse = ""  # Größe des Helms
preis = ""  # Preis des Helms
kategorie = ""  # Kategorie des Helms (z. B. Fahrradhelm, Motorradhelm)
verschluss = ""  # Verschlussart des Helms (z. B. Schnalle, Magnet)
material = ""  # Material des Helms (z. B. Kunststoff, Carbon)

# Strings, die später mit Helm-Optionen gefüllt werden
HelmKategorien: str = ""  # Speichert eine Liste aller Kategorien
HelmSize = ""  # Speichert eine Liste aller Größen
HelmLock = ""  # Speichert eine Liste aller Verschlüsse
HelmMaterial = ""  # Speichert eine Liste aller Materialien

# Liste, um passende Helme zu speichern
ConfirmedHelmet = []

def generateHelmCategories():
    """
    Diese Funktion erstellt eine Liste mit allen Helm-Kategorien und nummeriert sie.
    So kann man später leichter eine Kategorie auswählen.
    """
    global HelmKategorien  # Wir greifen auf die globale Variable zu.
    index = 0  # Startwert für die Nummerierung
    for helmKategorie in Helm.HelmKategorien:  # Wir gehen alle Helm-Kategorien durch.
        HelmKategorien += str(index) + f". {helmKategorie}\n"  # Nummer + Kategorie hinzufügen
        index += 1  # Nummer um 1 erhöhen

def generateHelmSize():
    """
    Diese Funktion erstellt eine nummerierte Liste mit allen verfügbaren Helmgrößen.
    """
    global HelmSize
    index = 0
    for helmSize in Helm.HelmSize:  # Wir gehen alle Größen durch.
        HelmSize += str(index) + f". {helmSize}\n"
        index += 1

def generateHelmLock():
    """
    Diese Funktion erstellt eine nummerierte Liste mit allen Helmverschlüssen.
    """
    global HelmLock
    index = 0
    for helmLock in Helm.HelmVerschluss:  # Wir gehen alle Verschlussarten durch.
        HelmLock += str(index) + f". {helmLock}\n"
        index += 1

def generateHelmMaterial():
    """
    Diese Funktion erstellt eine nummerierte Liste mit allen Helm-Materialien.
    """
    global HelmMaterial
    index = 0
    for helmMaterial in Helm.HelmMaterial:  # Wir gehen alle Materialien durch.
        HelmMaterial += str(index) + f". {helmMaterial}\n"
        index += 1

def getHelmets():
    """
    Diese Funktion sucht passende Helme basierend auf der Benutzer-Auswahl.
    Es wird überprüft, ob der Helm zur gewählten Kategorie, Größe, Material und Verschlussart passt.
    Wenn der Helm verfügbar ist und der Preis passt, wird er zur Liste 'ConfirmedHelmet' hinzugefügt.
    """
    for key in HelmBestand.helme:  # Wir gehen alle Helme aus dem Bestand durch.
        helm = HelmBestand.helme[key]  # Der aktuelle Helm
        # Überprüfung, ob der Helm zur Auswahl passt und auf Lager ist.
        if (helm.art == kategorie and helm.groesse == groesse and 
            helm.material == material and helm.verschluss == verschluss and 
            helm.preis <= preis and helm.warenbestand > 0):
            ConfirmedHelmet.append(key)  # Helm wird zur Liste hinzugefügt.

def generateStrings():
    """
    Diese Funktion ruft alle Funktionen auf, die Listen mit Helm-Optionen erstellen.
    Sie dient als Start-Funktion, damit alle Optionen bereitstehen.
    """
    generateHelmCategories()
    generateHelmLock()
    generateHelmMaterial()
    generateHelmSize()
