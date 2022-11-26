""""
Code zur Berechnung des groessten gemeinsamen Teilers und
des kleinsten gemeinsamen Vielfaches von zwei ganzen Zahlen
Lecture: Einfuehrung in das wissenschaftliche Rechnen
Authors: Thibaud Joel Hadamczik, Thomas Hoefting (2019)
"""

def ggt(zahl1, zahl2):
    """
    Funktion berechnet den groessten gemeinsamen Teiler von zwei ganzen Zahlen
    Args:
        zahl1(int): die erste Zahl
        zahl2(int): die zweite Zahl
    Returns:
        den groessten gemeinsamen der beiden eingegebenen Zahlen
    """
    rest = 1
    while rest != 0:
        rest = zahl1 % zahl2
        zahl1 = zahl2
        zahl2 = rest
    return zahl1

def kgv(zahl_a, zahl_b):
    """
    Funktion berechnet kleinstes gemeinsame Vielfache von zwei ganzen Zahlen
    Args:
        zahl_a(int): die erste Zahl
        zahl_b(int): die zweite Zahl
    Returns:
        das kleinste gemeinsame Vielfache der beiden eingegebenen Zahlen
    """
    return int((zahl_a * zahl_b) / ggt(zahl_a, zahl_b))


def main():
    """
    Hauptprogramm: Interaktion mit dem Nutzer(Eingabe vom Nutzer,Ausgabe vom Nutzer),
    Args: -
    Returns: -
    """
    zahl_a = int(input("Gebe die erste natürliche Zahl ein: "))
    zahl_b = int(input("Gebe die zweite natürliche Zahl ein: "))
    print("Der ggT von " + str(zahl_a) + " und " + str(zahl_b) + " ist " + str(ggt(zahl_a, zahl_b)))
    print("Das kgV von " + str(zahl_a) + " und " + str(zahl_b) + " ist " + str(kgv(zahl_a, zahl_b)))

if __name__ == '__main__':
    main()
