# Wir importieren die Klasse "shoppingCart" aus einer anderen Datei.
from ShoppingCart.shoppingCart import shoppingCart  

# Wir importieren das "os"-Modul, damit wir mit Dateien und Pfaden arbeiten können.
import os  

# Hier legen wir den Speicherort der Datei "user.txt" fest. 
# Diese Datei wird benutzt, um Benutzerdaten zu speichern.
path = os.path.join("./../", "user.txt")  

# Wir erstellen eine Klasse namens "user". Eine Klasse ist wie eine Bauanleitung für Objekte.
class user():
    # Die __init__-Funktion wird aufgerufen, wenn wir einen neuen Benutzer erstellen.
    # Sie speichert alle wichtigen Informationen über den Benutzer.
    def __init__(self, email, name, password, adresse, tel):
        # Jeder Benutzer hat einen eigenen Einkaufswagen.
        self.shoppingCart = shoppingCart()  
        
        # Die Informationen des Benutzers werden gespeichert:
        self.email = email  # E-Mail-Adresse
        self.name = name  # Name des Benutzers
        self.password = password  # Passwort (sollte sicher gespeichert werden!)
        self.adresse = adresse  # Wohnadresse
        self.tel = tel  # Telefonnummer

    # Diese Funktion speichert die Benutzerdaten in einer Datei.
    def speichern(self):
        # Zeigt den Dateipfad an (nur zur Kontrolle).
        print(path)  
        
        # Öffnet die Datei "user.txt" im Modus "+a" (Anhängen von Daten).
        save = open(path, "+a")  
        
        try:
            # Schreibt die Benutzerdaten Zeile für Zeile in die Datei.
            save.writelines([
                f"{self.name}\n", 
                f"{self.email}\n", 
                f"{self.name}\n",  # Achtung: Der Name wird hier zweimal gespeichert!
                f"{self.password}\n", 
                f"{self.adresse}\n", 
                f"{self.tel}\n"
            ])  
            # Schließt die Datei nach dem Schreiben.
            save.close()  
        except Exception as error:
            # Falls ein Fehler passiert, wird er ausgegeben.
            print(error)  
            # Die Datei wird trotzdem geschlossen.
            save.close()  
