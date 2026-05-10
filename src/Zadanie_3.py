import os

PLIK_WYNIKOWY = "wyniki3.txt"


def Zapisz_rozwiazanie_2_podzadan():
    if os.path.exists(PLIK_WYNIKOWY):
        os.unlink(PLIK_WYNIKOWY)

    Rozwiazanie_3_1("dane maj 23\\dron.txt")
    Rozwiazanie_3_2("dane maj 23\\dron.txt")


def nwd(a, b):
    if b == 0:
        return a

    while b != 0:
        c = a % b
        a = b
        b = c

    return a


def Rozwiazanie_3_1(sciezka):
    dane = []
    with open(sciezka, "r") as plik:
        dane = [line.rstrip("\n") for line in plik.readlines()]

    licznik = 0

    for linijka in dane:
        a, b = linijka.split(" ")
        wynik = nwd(abs((int)(a)), abs((int)(b)))
        if wynik > 1:
            licznik += 1

    with open("wyniki3.txt", "a") as plik:
        plik.write(f"Zadanie 3.1 wynik: {licznik}\n")


def Rozwiazanie_3_2(sciezka):
    dane = []
    with open(sciezka, "r") as plik:
        dane = [line.rstrip("\n") for line in plik.readlines()]

    punkty = [(0, 0)]
    index_punktow = 0

    for linijka in dane:
        a, b = linijka.split(" ")
        a = (int)(a)
        b = (int)(b)
        punkty.append((punkty[index_punktow][0] + a,
                      punkty[index_punktow][1] + b))

        index_punktow += 1

    kwadrat = [(0, 0), (0, 5000), (5000, 5000), (5000, 0)]

    odp_a = 0

    for punkt in punkty:
        if punkt[0] > kwadrat[0][0] and punkt[1] > kwadrat[0][1] and \
                punkt[0] > kwadrat[1][0] and punkt[1] < kwadrat[1][1] and \
                punkt[0] < kwadrat[2][0] and punkt[1] < kwadrat[2][1] and \
                punkt[0] < kwadrat[3][0] and punkt[1] > kwadrat[3][1]:
            odp_a += 1

    odp_b = None

    for index_jeden in range(len(punkty)):

        punkt_jeden = punkty[index_jeden]
        for index_dwa in range(index_jeden + 1, len(punkty)):

            punkt_dwa = punkty[index_dwa]
            for index_trzy in range(index_dwa + 1, len(punkty)):

                punkt_trzy = punkty[index_trzy]
                if ((punkt_jeden[0] + punkt_dwa[0]) / 2 == punkt_trzy[0] and (punkt_jeden[1] + punkt_dwa[1]) / 2 == punkt_trzy[1]) or \
                    ((punkt_jeden[0] + punkt_trzy[0]) / 2 == punkt_dwa[0] and (punkt_jeden[1] + punkt_trzy[1]) / 2 == punkt_dwa[1]) or \
                        ((punkt_trzy[0] + punkt_dwa[0]) / 2 == punkt_jeden[0] and (punkt_trzy[1] + punkt_dwa[1]) / 2 == punkt_jeden[1]):
                    odp_b = (punkt_jeden, punkt_dwa, punkt_trzy)
                    break

    with open("wyniki3.txt", "a") as plik:
        plik.write(f"Zadanie 3.2 a wynik: {odp_a}\n")
        plik.write(f"Zadanie 3.2 b wynik: {odp_b}\n")
