"""
Code zur Erstellung einer Klasse 'Bruch' zur Addition von Bruechen und deren
Ausgabe
Lecture: Einfuehrung in das wissenschaftliche Rechnen
Authors: Thibaud Joel Hadamczik, Thomas Hoefting (2019)
"""

from tools3 import ggt, kgv

class Bruch:
    """ ist eine Darstellung einer rationalen Zahl als gekuerzter Bruch
        Attributes:
            vorzeichen(bool): Wahrheitswert mit "True" falls der Bruch ein "-"
            als Vorzeichen hat und "False" falls nicht.
            zaehler(int): Der ganzzahlige Betrag des Zählers des Bruchs.
            nenner(int): Der ganzzahlige Betrag des Nenners des Bruchs.

    """

    def __init__(self, zaehler, nenner):
        """
        Initiiert die Klasse Bruch
        Args:
            zaehler(int): ein ganzzahliger Wert, der den Zaehler des Bruchs darstellt.
            nenner(int): ein ganzzahliger Wert, der den Nenner des Bruchs darstellt.

        Raises:
            ZeroDivisionError: gibt einen Fehler aus, falls der uebergebene
                               Zaehler sich nicht durch den Nenner teilen lässt,
                               da dieser 0 ist.
        """
        if nenner == 0:
            raise ZeroDivisionError("ZeroDivisionError!")

        self.vorzeichen = bool(zaehler/nenner < 0)
        self.zaehler = abs(zaehler)
        self.nenner = abs(nenner)

        self.kuerzen()

    def kuerzen(self):
        """
        kuerzt einen Bruch
        Args: None

        Returns:
            den Bruch in gekuerzter Form
        """
        ggt1 = ggt(self.zaehler, self.nenner)
        self.zaehler = int(self.zaehler/ggt1)
        self.nenner = int(self.nenner/ggt1)

    def summe(self, bruch_b):
        """
        addiert einen Bruch zu einem Bruch
        Args:
            bruch_b: ein Objekt der Klasse Bruch welches zu dem Bruch,
            auf den die Methode angewendet wird, addiert wird
        Returns:
            (Bruch) Ein Objekt der Klasse Bruch, welches die Summe des Bruches,
             auf welchen die Methode angewendet wird und des Inputparameters ist.
        """
        if self.vorzeichen is True:
            vorzeichen_a = -1
        else:
            vorzeichen_a = 1
        if bruch_b.vorzeichen is True:
            vorzeichen_b = -1
        else:
            vorzeichen_b = 1

        nenner = kgv(self.nenner, bruch_b.nenner)
        zaehler = (vorzeichen_a * self.zaehler * nenner / self.nenner) \
                  + (vorzeichen_b * bruch_b.zaehler * nenner / bruch_b.nenner)

        return Bruch(zaehler, nenner)

    def __add__(self, other):
        """
        ueberschreiben von add, sodass zwei Objekte der Klasse Bruch sinnvoll addiert werden
        """
        return self.summe(other)

    def __str__(self):
        """
        gibt eine String Repräsentation dieses Bruchs, die mit print()
        ausgegeben werden kann.
        """
        result = ""

        if self.vorzeichen is True:
            result = "- "

        result += str(self.zaehler)
        if self.nenner != 1:
            result += "/"
            result += str(self.nenner)

        return result

def main():
    """
    fuehrt die Additon zweier Brueche aus, und gibt das Ergebnis aus.
    """
    bruch_summe = Bruch(3, 7) + (Bruch(4, 9))
    print("Dies Summe von 3/7 und 4/9 ist = " + str(bruch_summe) + ".")
    bruch1 = input("Gebe Zaehler und Nenner des \
ersten Bruch durch ein Leerzeichen getrennt ein: ").split()
    bruch1 = (int(bruch1[0]), int(bruch1[1]))
    while bruch1[1] == 0:
        neuer_nenner1 = int(input("Gebe den Nenner des ersten Bruchs ein, \
der ungleich 0 sein muss: "))
        bruch1 = (int(bruch1[0]), neuer_nenner1)

    bruch2 = input("Gebe Zaehler und Nenner \
des zweiten Bruchs durch ein Leerzeichen getrennt ein: ").split()
    bruch2 = (int(bruch2[0]), int(bruch2[1]))
    while bruch2[1] == 0:
        neuer_nenner2 = int(input("Gebe den Nenner des zweiten Bruchs ein, \
der ungleich 0 sein muss: "))
        bruch2 = (bruch2[0], neuer_nenner2)

    bruch_summe = Bruch(bruch1[0], bruch1[1]) + Bruch(bruch2[0], bruch2[1])
    print("Die Summe der beiden Brueche ist " + str(bruch_summe) + ".")

if __name__ == '__main__':
    main()
