import os

LICZBY = [316498, 43657688, 154005710, 998877665544321]
PLIK_WYJSCIOWY = "wyniki1.txt"


def Zapisz_Rozwiazanie_3_Podzadan():
    if os.path.exists(PLIK_WYJSCIOWY):
        os.unlink(PLIK_WYJSCIOWY)

    Rozwiazanie_1_1()
    Rozwiazanie_1_2()
    Rozwiazanie_1_3()


def przestaw(n):
    r = n % 100
    a = r // 10
    b = r % 10
    n = n // 100

    w = None

    if n > 0:
        w = a + 10 * b + 100 * przestaw(n)
    else:
        if a > 0:
            w = a + 10 * b
        else:
            w = b

    return w


def przestaw2(n, do_print=False):
    rezultat = __przestaw2(n, 1)

    if do_print:
        return rezultat

    return rezultat[0]


def __przestaw2(n, l):
    r = n % 100
    a = r // 10
    b = r % 10
    n = n // 100

    w = None

    if n > 0:
        rezultat = __przestaw2(n, l + 1)
        l = rezultat[1]
        w = a + 10 * b + 100 * rezultat[0]
    else:
        if a > 0:
            w = a + 10 * b
        else:
            w = b

    return w, l


def przestaw_nie_rekurencyjnie(n):

    granica = 0
    n2 = n

    while n2 > 0:
        granica += 1
        n2 = n2 // 10

    w = 0

    for i in range(0, (2 * granica + 1) // 2, 2):
        r = n % 100
        a = r // 10
        b = r % 10
        n = n // 100

        if a > 0:
            w = w + b * 10 ** (i + 1) + a * 10 ** i
        else:
            w = w + b * 10 ** i

    return w


def Rozwiazanie_1_1():
    LICZBY = [316498, 43657688, 154005710, 998877665544321]

    with open("wyniki1.txt", "a") as plik:
        plik.write("rozwiazanie Zadania 1.1:\n")

        for liczba in LICZBY:
            rezultat = przestaw2(liczba, True)
            plik.write("Rezultat dla liczba = " + str(liczba) + "to wynik = " +
                       str(rezultat[0]) + " i wywolan = " + str(rezultat[1]) + "\n")

        plik.write("\n")


def Rozwiazanie_1_2():
    rezultaty = []

    for i in range(len(LICZBY)):
        liczba = LICZBY[i]

        x = liczba
        k = 0

        while x > 0:
            x = x // 10
            k = k + 1

        rezultat = []

        rezultat.append(("k / 2 == przestaw2(" + str(liczba) +
                        ")[1]", k / 2 == przestaw2(liczba, True)[1]))
        rezultat.append(("(k + 1) div 2 == przestaw2(" + str(liczba) +
                        ")[1]", (k + 1) // 2 == przestaw2(liczba, True)[1]))
        rezultat.append(("k/2 if k / 2 == 0 else (k + 1) // 2  == przestaw2(" + str(liczba) +
                        ")[1]", k/2 if k % 2 == 0 else (k +
                                                        1) / 2 == przestaw2(liczba, True)[1]))
        rezultat.append(("(k + 1) / 2 == przestaw2(" + str(liczba) + ")[1]", (k +
                                                                              1) / 2 == przestaw2(liczba, True)[1]))
        rezultaty.append(rezultat)

    jest_jeden = rezultat[0][1]
    jest_dwa = rezultat[1][1]
    jest_trzy = rezultat[2][1]
    jest_cztery = rezultat[3][1]

    with open(PLIK_WYJSCIOWY, "a") as plik:
        plik.write("Rozwiazanie Zadania 1.2:\n")
        plik.write("Jeden jest = " + str(jest_jeden) + "\n")
        plik.write("Dwa jest = " + str(jest_dwa) + "\n")
        plik.write("Trzy jest = " + str(jest_trzy) + "\n")
        plik.write("Cztery jest = " + str(jest_cztery) + "\n")
        plik.write("\n")


def Rozwiazanie_1_3():
    with open(PLIK_WYJSCIOWY, "a") as plik:
        plik.write("Rzoawiazanie Zadanie 1.3:\n")
        for liczba in LICZBY:
            rezultat1 = przestaw(liczba)
            rezultat2 = przestaw_nie_rekurencyjnie(liczba)
            plik.write("liczba = " + str(liczba) + ", przestaw(" + str(liczba) + ") = " + str(rezultat1) +
                       ", przestaw_nie_rekurencyjnie(" + str(liczba) + ") = " + str(rezultat2) + ", czy rowne = " + str(rezultat1 == rezultat2) + "\n")
