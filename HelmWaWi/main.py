# Importieren von Modulen für die Benutzeransicht.
#from HelmWaWi.Controller import Logic  # (Aktuell auskommentiert, könnte für die Helmauswahl sein.)
#from HelmWaWi.View import View  # (Aktuell auskommentiert, könnte für die Anzeige der Helme sein.)
from User.View import userView  # Importiert die Benutzeransicht für die Registrierung.

"""
Dieses Skript ist der Startpunkt des Programms.
Hier wird Schritt für Schritt festgelegt, welche Abläufe gestartet werden.
"""

# Die folgenden Zeilen sind auskommentiert, könnten aber für die Helmauswahl genutzt werden:
# Logic.generateStrings()  # Erstellt die Auswahlmöglichkeiten für Helme.
# View.getInput()  # Fragt den Benutzer nach seinen Helm-Wünschen.
# Logic.getHelmets()  # Sucht passende Helme basierend auf der Benutzerauswahl.
# View.printHelmet()  # Gibt die gefundenen Helme aus.

# Hier startet die Benutzerregistrierung.
userView.getUserData()  # Fragt den Benutzer nach seinen Daten und erstellt ein neues Konto.
