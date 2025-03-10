from Model import Helm  # Wir importieren das Helm-Modul, damit wir Helme erstellen können.

"""
Dieses Skript funktioniert wie eine kleine Datenbank für Helme.
Hier speichern wir viele verschiedene Helme mit ihren Eigenschaften.
"""

# Ein Wörterbuch (Dictionary), das verschiedene Helme speichert.
# Jeder Helm hat einen Namen als Schlüssel und ein Helm-Objekt als Wert.
helme = {
    "Storm Racer": Helm.Helm("Storm Racer", "M", 5, 150, "Sport", "Ratsche", "Polycarbonat"),
    "Mountain King": Helm.Helm("Mountain King", "L", 2, 220, "Enduro", "Doppel-D", "Carbon"),
    "Cruiser Pro": Helm.Helm("Cruiser Pro", "XL", 3, 180, "Cruiser", "Ratsche", "Fiberglas"),
    "Urban Jet": Helm.Helm("Urban Jet", "S", 4, 120, "Jethelm", "Ratsche", "Polycarbonat"),
    "Touring Master": Helm.Helm("Touring Master", "M", 6, 250, "Klapphelm", "Doppel-D", "Fiberglas"),
    "Speedster": Helm.Helm("Speedster", "L", 7, 200, "Sport", "Ratsche", "Carbon"),
    "Desert Storm": Helm.Helm("Desert Storm", "M", 5, 230, "Enduro", "Doppel-D", "Polycarbonat"),
    "Classic Cruiser": Helm.Helm("Classic Cruiser", "XL", 2, 170, "Cruiser", "Ratsche", "Fiberglas"),
    "City Rider": Helm.Helm("City Rider", "S", 8, 110, "Jethelm", "Ratsche", "Polycarbonat"),
    "Adventure Pro": Helm.Helm("Adventure Pro", "L", 3, 260, "Klapphelm", "Doppel-D", "Carbon"),
    "Track Master": Helm.Helm("Track Master", "M", 4, 190, "Sport", "Ratsche", "Fiberglas"),
    "Offroad Beast": Helm.Helm("Offroad Beast", "L", 5, 240, "Enduro", "Doppel-D", "Carbon"),
    "Road King": Helm.Helm("Road King", "XL", 3, 210, "Cruiser", "Ratsche", "Polycarbonat"),
    "Night Hawk": Helm.Helm("Night Hawk", "S", 7, 140, "Jethelm", "Ratsche", "Fiberglas"),
    "Falcon GT": Helm.Helm("Falcon GT", "M", 6, 270, "Klapphelm", "Doppel-D", "Carbon"),
    "Speed Demon": Helm.Helm("Speed Demon", "L", 5, 220, "Sport", "Ratsche", "Polycarbonat"),
    "Dirt Blazer": Helm.Helm("Dirt Blazer", "M", 4, 250, "Enduro", "Doppel-D", "Fiberglas"),
    "Sunset Cruiser": Helm.Helm("Sunset Cruiser", "XL", 3, 180, "Cruiser", "Ratsche", "Carbon"),
    "City Hawk": Helm.Helm("City Hawk", "S", 9, 130, "Jethelm", "Ratsche", "Polycarbonat"),
    "Elite Touring": Helm.Helm("Elite Touring", "M", 7, 280, "Klapphelm", "Doppel-D", "Fiberglas"),
    "Speed Viper": Helm.Helm("Speed Viper", "L", 6, 200, "Sport", "Ratsche", "Carbon"),
    "Enduro X": Helm.Helm("Enduro X", "M", 5, 260, "Enduro", "Doppel-D", "Polycarbonat"),
    "Thunder Cruiser": Helm.Helm("Thunder Cruiser", "XL", 4, 190, "Cruiser", "Ratsche", "Fiberglas"),
    "Street Rebel": Helm.Helm("Street Rebel", "S", 8, 120, "Jethelm", "Ratsche", "Polycarbonat"),
    "Globetrotter": Helm.Helm("Globetrotter", "M", 6, 270, "Klapphelm", "Doppel-D", "Carbon"),
    "Velocity Storm": Helm.Helm("Velocity Storm", "L", 5, 230, "Sport", "Ratsche", "Polycarbonat"),
    "Trail Master": Helm.Helm("Trail Master", "M", 4, 250, "Enduro", "Doppel-D", "Fiberglas"),
    "Blitz Racer": Helm.Helm("Blitz Racer", "L", 6, 200, "Sport", "Ratsche", "Carbon"),
    "Wild Roamer": Helm.Helm("Wild Roamer", "M", 5, 260, "Enduro", "Doppel-D", "Polycarbonat"),
    "Neon Speed": Helm.Helm("Neon Speed", "S", 8, 120, "Jethelm", "Ratsche", "Polycarbonat"),
    "Hyper Rider": Helm.Helm("Hyper Rider", "M", 5, 250, "Sport", "Ratsche", "Fiberglas"),
    "Desert Hawk": Helm.Helm("Desert Hawk", "L", 4, 240, "Enduro", "Doppel-D", "Carbon"),
    "Night Racer": Helm.Helm("Night Racer", "XL", 3, 200, "Cruiser", "Ratsche", "Polycarbonat"),
    "Comet Jet": Helm.Helm("Comet Jet", "S", 7, 110, "Jethelm", "Ratsche", "Fiberglas"),
    "Shadow Touring": Helm.Helm("Shadow Touring", "M", 6, 275, "Klapphelm", "Doppel-D", "Carbon"),
    "Lightning Speed": Helm.Helm("Lightning Speed", "L", 5, 225, "Sport", "Ratsche", "Polycarbonat"),
    "Speed Phantom": Helm.Helm("Speed Phantom", "M", 4, 210, "Sport", "Ratsche", "Fiberglas"),
    "Extreme Ride": Helm.Helm("Extreme Ride", "XL", 5, 260, "Enduro", "Doppel-D", "Carbon"),
    "Urban Explorer": Helm.Helm("Urban Explorer", "S", 6, 170, "Jethelm", "Ratsche", "Polycarbonat"),
    "Classic Heritage": Helm.Helm("Classic Heritage", "L", 3, 200, "Cruiser", "Ratsche", "Fiberglas"),
}
