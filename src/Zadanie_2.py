import os


SLOWNIK = {"o": 0, "+": 1, "*": 2}
PLIK_WYJSCIOWY = "wyniki2.txt"


def Zapisz_Rozwiazanie_4_Podzadan():
    if os.path.exists(PLIK_WYJSCIOWY):
        os.unlink(PLIK_WYJSCIOWY)

    Rozwiazanie_2_1()
    Rozwiazanie_2_2()
    Rozwiazanie_2_3()
    Rozwiazanie_2_4()


def __trojkowy_do_dziesietny(trojkowy):
    baza = 1
    suma = 0
    for i in range(len(trojkowy) - 1, -1, -1):
        suma += baza * SLOWNIK[trojkowy[i]]
        baza = baza * 3

    return suma


def __dziesietny_do_trojkowy(dziesietny):
    rezultat = []

    while dziesietny > 0:
        wy = dziesietny % 3
        v = [k for k, v in SLOWNIK.items() if v == dziesietny % 3][0]

        rezultat.append(v)
        dziesietny = dziesietny // 3

    rezultat.reverse()
    return "".join(rezultat)


def __przygotuj_dane():
    linijki = []
    linijki.clear()
    with open("dane maj 23\\symbole.txt", 'r') as f:
        for linijka in f:
            linijka = linijka[:-1]
            linijki.append(linijka)

    return linijki


def __czy_palindrom(linijka):

    for i in range(len(linijka)):
        if linijka[i] != linijka[len(linijka) - 1 - i]:
            return False

    return True


def Rozwiazanie_2_1():

    with open(PLIK_WYJSCIOWY, "a") as plik:
        plik.write("Rozwiazanie Zadanie 2.1:\n")
        for linijka in __przygotuj_dane():
            if __czy_palindrom(linijka):
                plik.write(linijka + "\n")

        plik.write("\n")


def Rozwiazanie_2_2():

    linijki = __przygotuj_dane()
    licznik = 0

    with open(PLIK_WYJSCIOWY, "a") as plik:
        plik.write("Rozwiazanie Zadania 2.2:\n")
        for i in range(len(linijki) - 2):

            linijka1 = linijki[i]
            linijka2 = linijki[i + 1]
            linijka3 = linijki[i + 2]

            for j in range(len(linijka1) - 2):

                zbior = set()
                for znak in linijka1[j: j + 3]:
                    zbior.add(znak)
                for znak in linijka2[j: j + 3]:
                    zbior.add(znak)
                for znak in linijka3[j: j + 3]:
                    zbior.add(znak)

                if len(zbior) == 1:
                    licznik += 1
                    plik.write(str((licznik, i + 2, j + 2)) + "\n")

        plik.write("\n")


def Rozwiazanie_2_3():
    max_suma = 0
    max_linijka = ""

    for linijka in __przygotuj_dane():
        suma = __trojkowy_do_dziesietny(linijka)

        if suma > max_suma:
            max_suma = suma
            max_linijka = linijka

    with open(PLIK_WYJSCIOWY, "a") as plik:
        plik.write("Rozwiazanie Zadania 2.3:\n")
        plik.write(str((max_suma, max_linijka)) + "\n")
        plik.write("\n")


def Rozwiazanie_2_4():
    __przygotuj_dane()

    suma = 0

    for linijka in __przygotuj_dane():
        suma += __trojkowy_do_dziesietny(linijka)

    with open(PLIK_WYJSCIOWY, "a") as plik:
        plik.write("Rozwiazanie Zadanie 2.4:\n")

        plik.write(str((suma, __dziesietny_do_trojkowy(suma))))
