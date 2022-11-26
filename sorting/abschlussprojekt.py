"""
Code zum Einlesen einer Datei mit durch Leerzeichen getrennten Woertern,
Speicherung der Woerter in einer Liste, Sortierung der Liste mittels der
Sortierverfahren mergesort und combsort sowie
zur statistischen Auswertung der Sortierverfahren

Lecture: Einfuehrung in das wissenschaftliche Rechnen
Authors: Thibaud Joel Hadamczik, Thomas Hoefting (2019)
"""

import time

def input_processing(file_location):
    """
    Funktion speichert alle durch Leerzeichen getrennten Woerter der unter
    dem als Eingabeparameter angegebenen Pfad
    gespeicherten (Text-)Datei in einer Liste
    Args:
        file_location(str): Pfad zu  der Datei, deren Inhalt als Liste
                            gespeichert werden soll
    Returns:
        (list[str]): Eine Liste mit allen durch Leerzeichen (inkl. whitespace,
                     tabstop, newline) getrennten Strings der Datei
    """
    file = open((file_location), "r")
    text = file.read()
    file.close()
    word_list = text.split(" ")
    for word in word_list:
        if word.find("\n") > -1:
            word_list[word_list.index(word):word_list.index(word)] \
                = word.split("\n")
            word_list.remove(word)
    for word in word_list:
        if word.find("\t") > -1:
            word_list[word_list.index(word):word_list.index(word)] \
                = word.split("\t")
            word_list.remove(word)
    word_list = [word for word in word_list if word != ""]
    return word_list

def mergesort(word_list):
    """
    Funktion sortiert eine in der als Eingabeparameter uebergebenen
    Liste von Strings mittels des Sortierverfahrens mergesort
    Args:
        word_list(list[str]): die Liste mit den zu sortierenden Wörtern
    Returns:
        sorted_list(list[str]): die sortierte Liste
        comparisons(int): Anzahl der durchgefuehrten Vergleiche
    """
    comparisons = 0
    if len(word_list) <= 1:
        return word_list, comparisons
    sorted_list = []
    mid = int(len(word_list) / 2)
    left_half = mergesort(word_list[:mid])
    right_half = mergesort(word_list[mid:])
    comparisons = left_half[1] + right_half[1]
    left_half = left_half[0]
    right_half = right_half[0]
    iterator1 = 0
    iterator2 = 0
    while iterator1 < len(left_half) and iterator2 < len(right_half):
        if left_half[iterator1] <= right_half[iterator2]:
            sorted_list.append(left_half[iterator1])
            iterator1 += 1
        else:
            sorted_list.append(right_half[iterator2])
            iterator2 += 1
        comparisons += 1
    sorted_list = sorted_list + left_half[iterator1:] + right_half[iterator2:]
    return sorted_list, comparisons

def combsort(word_list):
    """
    Die Funktion sortiert eine Liste übergebener Wörter mit dem
    Combsort-Algorithmus.
    Args:
        word_list(list[str]): die Liste mit den zu sortierenden Wörtern
    Returns:
        word_list(list[str]): die sortierte Liste
        sum_swaps_comps(int): Die Summe der Vertauschungen und Vergleiche
    """
    gap = len(word_list)
    is_swapped = False
    swaps = 0
    comparisons = 0
    while is_swapped is True or gap > 1:
        is_swapped = False
        if gap > 1:
            gap = int(gap/1.3)
        for word_index in range(len(word_list)- gap):
            if word_list[word_index] > word_list[word_index + gap]:
                word_list[word_index], word_list[word_index + gap] \
                    = word_list[word_index + gap], word_list[word_index]
                is_swapped = True
                swaps += 1
            comparisons += 1
    sum_swaps_comps = swaps + comparisons
    return word_list, sum_swaps_comps

def sort_A(word_list):
    """
    Funktion zur Analyse der Komplexität von mergesort
    Args:
        word_list(list[str]): die Liste mit den zu sortierenden Strings
    Returns:
        comparisons(int): Anzahl der bei der Ausfuehrung des
                          Algorithmus durchgefuehrten Vergleiche
        used_time(float): die fuer die Ausfuehrung des
                          Sortieralgorithmus benoetigte Zeit in Millisekunden
    """
    time_start = time.clock()
    comparisons = mergesort(word_list)[1]
    time_end = time.clock()
    used_time = (time_end-time_start)*1000
    return comparisons, used_time

def sort_B(word_list):
    """
    Funktion zur Analyse von Komplexität von combsort
    Args:
        word_list(list[str]): die Liste mit den zu sortierenden Strings
    Returns:
        sum_swaps_comps(int): Summe der bei der Ausfuehrung des
                              Sortieralgorithmus durchgefuehrten
                              Vergleiche und Vertauschungen
        used_time(float): die fuer die Ausfuehrung des Sortieralgorithmus
                          benoetigte Zeit in Millisekunden
    """
    time_start = time.clock()
    sum_swaps_comps = combsort(word_list)[1]
    time_end = time.clock()
    used_time = (time_end - time_start)*1000
    return sum_swaps_comps, used_time

def main():
    """
        Interaktion mit dem Nutzer zur Eingabe der zu sortierenen Textdatei
        und Ausgabe der Analysedaten.
        Args: -
        Returns: -
    """
    file_location = str(input("Geben Sie den Pfad zur Datei ein, "
                              "die durch Leerzeichen getrennte Woerter enthaelt: "))
    file = input_processing(file_location)
    results_A = sort_A(file)
    results_B = sort_B(file)
    print(str(results_A))
    print(str(results_B))


if __name__ == '__main__':
    main()
