from datetime import datetime
import matplotlib.pyplot as plt
import os


PLIK_WYNIKOWY = "wyniki6.txt"
PLIK_WYKRESU = "wykres_6_4.jpg"


def Zapisz_rozwiazanie_5_podzadan():
    if os.path.exists(PLIK_WYNIKOWY):
        os.unlink(PLIK_WYNIKOWY)

    if os.path.exists(PLIK_WYKRESU):
        os.unlink(PLIK_WYKRESU)

    Rozwiazanie_6_1()
    Rozwiazanie_6_2()
    Rozwiazanie_6_3()
    Rozwiazanie_6_4()
    Rozwiazanie_6_5()


def wczytaj(sciezka="dane maj 23\\martianeum.txt"):

    linijki = None
    with open(sciezka, "r") as plik:
        linijki = plik.readlines()

    linijki.pop(0)
    return linijki


def przeprocesuj_linijki(linijki):
    przeprocesowane_dane = []
    for linijka in linijki:
        linijka = linijka.rstrip("\n")
        podzielone = linijka.split("\t")
        if len(podzielone) != 4:
            continue

        przeprocesowane_dane.append([datetime.strptime(
            podzielone[0], "%Y-%m-%d").date(), podzielone[1], (float)(podzielone[2].replace(",", ".")), (float)(podzielone[3].replace(",", "."))])

    return przeprocesowane_dane


def Rozwiazanie_6_1():
    linijki = wczytaj()
    dane = przeprocesuj_linijki(linijki)

    masa_ladunkow = sum([linijka[2] for linijka in dane])
    masa_wydobycia = sum([linijka[2] * linijka[3] / 100
                         for linijka in dane if linijka[3] >= 1])

    with open(PLIK_WYNIKOWY, "a") as plik:
        plik.write("6.1 Laczna masa ladunkow drona: " +
                   str(masa_ladunkow) + "\n")
        plik.write("6.1 Laczna masa martianeum: " + str(masa_wydobycia) + "\n")


def Rozwiazanie_6_2():
    linijki = wczytaj()
    dane = przeprocesuj_linijki(linijki)

    obszary = list(set([linijka[1] for linijka in dane]))
    obszary.sort()

    zestawienie = dict()

    for obszar in obszary:
        suma = sum([linijka[2] for linijka in dane if linijka[1] == obszar])
        liczebnosc = len([linijka for linijka in dane if linijka[1] == obszar])

        if suma == 0 and liczebnosc == 0:
            zestawienie[obszar] = 0
        else:
            zestawienie[obszar] = suma / liczebnosc

    min_obszar = obszary[0]
    min_wydobycie = zestawienie[min_obszar]

    for obszar, wydobycie in zestawienie.items():
        if wydobycie < min_wydobycie:
            min_wydobycie = wydobycie
            min_obszar = obszar

    with open(PLIK_WYNIKOWY, "a") as plik:
        plik.write(
            "6.2 Obszar o najnizszym srednim wydobyciu to: " + str(min_obszar) + "\n")


def Rozwiazanie_6_3():
    linijki = wczytaj()
    dane = przeprocesuj_linijki(linijki)

    okresy = [dane[start:start + 7]
              for start in range(0, len(dane) - 1, 7)]

    max_suma_ilosci = 0
    dane_max_sumy_ilosci = None

    for okres in okresy:
        suma_ilosci = sum(linia[2] for linia in okres)
        dane_max_sumy_ilosci = okres[0][0] if suma_ilosci > max_suma_ilosci else dane_max_sumy_ilosci
        max_suma_ilosci = suma_ilosci if suma_ilosci > max_suma_ilosci else max_suma_ilosci

    with open(PLIK_WYNIKOWY, "a") as plik:
        plik.write(
            "6.3 Maksymalna masa ladunkow w 7 dniowych okresach: " + str(max_suma_ilosci) + "\n")
        plik.write("6.3 Data pierwzszego dnia 7 dniowego okresu w ktorym bylo max ladunku: " +
                   str(dane_max_sumy_ilosci) + "\n")


def Rozwiazanie_6_4():
    linijki = wczytaj()
    data = przeprocesuj_linijki(linijki)

    obszary = list(set([linijka[1] for linijka in data]))
    obszary.sort()

    lata = list(set([linijka[0].year for linijka in data]))
    lata.sort()

    czestosci = dict()

    for obszar in obszary:
        for rok in lata:
            if not rok in czestosci.keys():
                czestosci[rok] = []
            czestosci[rok].append(sum(
                [1 for linijka in data if linijka[1] == obszar and linijka[0].year == rok]))

    N = len(obszary)

    fig, ax = plt.subplots()

    for rok in lata:
        ax.bar(obszary, czestosci[rok], 0.4, label=rok)

    ax.set_xticklabels(obszary)
    ax.legend()
    plt.xticks(rotation=65, ha='right')
    plt.savefig(PLIK_WYKRESU)


def Rozwiazanie_6_5():
    linijki = wczytaj()
    data = przeprocesuj_linijki(linijki)

    wydobycie = [(d[0], d[2] * d[3] / 100) for d in data if d[3] >= 1]

    skumulowane_wydobycie_minus_transporty = 0
    licznik = 0
    data_pierwszego_transprtu = None
    data_ostatniego_transportu = None

    for w in wydobycie:
        skumulowane_wydobycie_minus_transporty += w[1]
        if skumulowane_wydobycie_minus_transporty >= 100:
            skumulowane_wydobycie_minus_transporty -= 100
            licznik += 1
            if data_pierwszego_transprtu == None:
                data_pierwszego_transprtu = w[0]
            data_ostatniego_transportu = w[0]

    with open(PLIK_WYNIKOWY, "a") as plik:
        plik.write(
            "6.5 Stacja wyslala na orbite ladunek: " + str(licznik) + " razy.\n")
        plik.write("6.5 Data pierwszego transportu: " +
                   str(data_pierwszego_transprtu) + "\n")
        plik.write("6.5 Data ostatniego transprtu: " +
                   str(data_ostatniego_transportu) + "\n")
