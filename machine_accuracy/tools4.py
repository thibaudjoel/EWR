""""
Code mit Funktionen zur Durchführung der Experimente aus den Aufgaben 2 und 3
Lecture: Einfuehrung in das wissenschaftliche Rechnen
Authors: Thibaud Joel Hadamczik, Thomas Hoefting (2019)
"""
import decimal
import numpy as np
import matplotlib.pyplot as plt

def accuracy1(datatype):
    """
    berechnet die relative Maschinengenauigkeit für einen der Datentypen numpy.float64, numpy.float32 und numpy.float16
    Inputs: datatype(string): der Datentyp, für den die relative Maschinengenauigkeit bestimmt werden soll.
    Einer der Typen numpy.float64, numpy.float32 und numpyfloat.16
    Returns: genauigkeit(numpy.float) die relative Maschinengenauigkeit. Der Datentyp entspricht dem als Parameter
    übergebenden Datentyp.
    """
    genauigkeit = 1
    if datatype == "numpy.float64":
        startwert = np.float64(1)

        while np.float64(1 + startwert) != 1:
            genauigkeit = startwert
            startwert = startwert / np.float64(2)

    elif datatype == "numpy.float32":

        startwert = np.float32(1)

        while np.float32(1 + startwert) != 1:
            genauigkeit = startwert
            startwert = startwert / np.float32(2)

    elif datatype == "numpy.float16":
        startwert = np.float16(1)

        while np.float16(1) + startwert != 1:
            genauigkeit = startwert
            startwert = startwert / np.float16(2)

    return genauigkeit

def accuracy2(datatype):
    """
    berechnet die relative Maschinengenauigkeit für einen der Datentypen numpy.float64, numpy.float32 und numpy.float16
    Inputs: datatype(string): der Datentyp, für den die relative Maschinengenauigkeit bestimmt werden soll.
    Einer der Typen numpy.float64, numpy.float32 und numpy.float 16
    Returns: genauigkeit(numpy.float) die relative Maschinengenauigkeit. Der Datentyp entspricht dem als Parameter
    übergebenden Datentyp.
    """
    genauigkeit = 1
    if datatype == "numpy.float64":

        genauigkeit = np.float64(7/3) - np.float64(4/3) - np.float64(1)

    elif datatype == "numpy.float32":

        genauigkeit = np.float32(7/3) - np.float32(4/3) - np.float32(1)

    elif datatype == "numpy.float16":

        genauigkeit = np.float16(7)/np.float16(3) - np.float16(4)/np.float16(3) - np.float16(1)

    return genauigkeit


def experiment(wert, laenge):
    """
   Experiment der Funktion aus der Aufgabenstellung A3 mit Mantissenlaengeneingabe
    Inputs:
        wert(float): Der Wert der dem decimal übergeben werden soll
        laenge(int): Die Mantissenlaenge, fuer die die Berechnung erfolgen soll
    Returns:
        yl(decimal.Decimal): das Ergebnis der linken Seite der Gleichung aus A3
        yr(decimal.Decimal): das Ergebnis der rechten Seite der Gleichung aus A3
        fehler_absolut(decimal.Decimal): der absolute Fehler von yl und yr
        fehler_relativ(decimal.Decimal): der relative Fehler von yl und yr
    Raises:
        ZeroDivisionError: wird geworfen, wenn yl = 0 ist, und der relative
        Fehler somit nicht bestimmt werden kann.
    """
    decimal.getcontext().prec = laenge
    versuchsfall = decimal.Decimal(wert)
    yl = decimal.Decimal(1/versuchsfall - 1/(versuchsfall + 1))
    yr = decimal.Decimal(1/(versuchsfall*(versuchsfall + 1)))
    fehler_absolut = abs(float(yl) - float(yr))
    if float(yr) == 0:
        raise ZeroDivisionError ("Relativer Fehler kann nicht berechnet werden")
    else:
        fehler_relativ = abs(fehler_absolut/float(yr))

    return [yl, yr, fehler_absolut, fehler_relativ]

def plotten(x1, x2, x3):
    """
    Gibt die Ergebnisse des Experiments aus A3 grafisch aus.
    Inputs:
        x1(float): der erste x-Wert
        x2(float): der zweite x-Wert
        x3(float): der dritte x-Wert
    Returns:-
    """
    x = range(1, 25)
    y1 = []
    for i in x:
        y1.append(experiment(x1, i)[3])

    y2 = []
    for i in x:
        y2.append(experiment(x2, i)[3])

    y3 = []
    for i in x:
        y3.append(experiment(x3, i)[3])

    plt.plot(x, y1, label="x1")
    plt.plot(x, y2, label="x2")
    plt.plot(x, y3, label="x3")
    plt.xlabel('Mantissenlaenge')
    plt.ylabel('relativer Fehler')
    plt.yscale('log')
    plt.legend()
    plt.savefig("fig_all.png")
    plt.show()
print(accuracy1("numpy.float16"))
print(accuracy1("numpy.float32"))
print(accuracy1("numpy.float64"))