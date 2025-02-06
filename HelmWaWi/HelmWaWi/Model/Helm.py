class Helm:
    """
    Diese Klasse ist wie eine Bauanleitung für einen Helm.
    Sie speichert alle wichtigen Eigenschaften eines Helms.
    """

    def __init__(self, name, groesse, warenbestand, preis, art, verschluss, material):
        """
        Diese Funktion wird aufgerufen, wenn ein neuer Helm erstellt wird.
        Sie speichert alle Informationen über den Helm.
        """
        self.name = name  # Der Name des Helms (z. B. "Speedy 3000")
        self.groesse = groesse  # Die Größe des Helms (S, M, L, XL)
        self.warenbestand = warenbestand  # Wie viele Helme gibt es noch auf Lager?
        self.preis = preis  # Der Preis des Helms in Euro (€)
        self.art = art  # Die Art des Helms (z. B. Sporthelm, Endurohelm)
        self.verschluss = verschluss  # Der Verschluss des Helms (z. B. Ratsche oder Doppel-D)
        self.material = material  # Das Material des Helms (z. B. Fiberglas, Carbon)

    def __repr__(self):
        """
        Diese Funktion sorgt dafür, dass der Helm als Text dargestellt wird,
        wenn wir ihn z. B. ausdrucken oder in einer Liste speichern.
        """
        return (f"Helm(Name: {self.name}, Gr\u00f6\u00dfe: {self.groesse}, Warenbestand: {self.warenbestand}, "
                f"Preis: {self.preis}\u20ac, Art: {self.art}, Verschluss: {self.verschluss}, Material: {self.material})")

# Jetzt erstellen wir Listen mit den verschiedenen Helm-Optionen.

# Alle verfügbaren Helm-Kategorien:
HelmKategorien = ("Sport", "Enduro", "Cruiser", "Jethelm", "Klapphelm")

# Alle verfügbaren Größen:
HelmSize = ("S", "M", "L", "XL")

# Alle verfügbaren Verschlussarten:
HelmVerschluss = ("Ratsche", "Doppel-D")

# Alle verfügbaren Materialien:
HelmMaterial = ("Fiberglas", "Carbon", "Polycarbonat")
