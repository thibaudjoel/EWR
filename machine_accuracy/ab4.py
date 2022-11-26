""""
Code zum Einlesen einer daten.txt Datei mit 4 Zeilen, und Erstellen einer Graphik,
die den relativen Fehler der 3 Zahlen fuer
Mantissenlaengen von 1-25 darstellt, sowie die relative Maschinengenauigkeit in Abhaengigkeit
vom in der .txt Datei angegebenen Datentyp
Lecture: Einfuehrung in das wissenschaftliche Rechnen
Authors: Thibaud Joel Hadamczik, Thomas Hoefting (2019)
"""


from tools4 import *

def main():
    """
    Hauptprogramm: liest beim Starten des Programms die ersten 4 Zeilen einer Datei datei.txt, und
    gibt anhand der    entsprechenden Werte die relative Maschinengenauigkeit in Abhaengigkeit vom
    Datentyp aus sowie eine Graphik, die den relativen Fehler fuer verschiedene Werte der Mantissenlaenge
    abtraegt.
    Args: -
    Returns: -

    """
    fobj = open("daten.txt", "r")
    datentyp = fobj.readline()
    x1 = float(fobj.readline())
    x2 = float(fobj.readline())
    x3 = float(fobj.readline())
    laenge = int(fobj.readline())
    fobj.close()

    print("Die relative Maschinengenauigkeit beim Datentyp " + datentyp + " betraegt " + str(accuracy1(datentyp)))
    plotten(x1, x2, x3)
    print("relativer Fehler der beiden Seiten der Gleichung zu verschiedenen x-Werten: ")
    print("relativer Fehler bei Mantissenlänge = " + str(laenge) + " und x = " + str(x1) + ": " + str(experiment(x1, \
            laenge)[3]))
    print("relativer Fehler bei Mantissenlänge = " + str(laenge) + " und x = " + str(x2) + ": " + str(experiment(x2, \
            laenge)[3]))
    print("relativer Fehler bei Mantissenlänge = " + str(laenge) + " und x = " + str(x3) + ": " + str(experiment(x3, \
            laenge)[3]))

if __name__ == '__main__':
    main()
