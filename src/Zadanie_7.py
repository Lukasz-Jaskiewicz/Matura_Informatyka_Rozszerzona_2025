from datetime import date
import os
PLIK_WYNIKOWY = "wyniki7Pyt.txt"
DANE = {"obszary": "dane maj 23\\obszary.txt",
        "pomiary": "dane maj 23\\pomiary.txt", "laziki": "dane maj 23\\laziki.txt"}


def Zapisz_rozwiazanie_4_podzadan():
    if os.path.exists(PLIK_WYNIKOWY):
        os.unlink(PLIK_WYNIKOWY)

    Rozwiazanie_7_1()
    Rozwiazanie_7_2()
    Rozwiazanie_7_3()
    Rozwiazanie_7_4()


def __wczytaj_dane():

    obszary = [__procesuj_linijke_obszarow(
        linijka) for linijka in __wczytaj_pojedynczy_plik(DANE["obszary"])]
    pomiary = [__procesuj_linijke_pomiarow(
        linijka) for linijka in __wczytaj_pojedynczy_plik(DANE["pomiary"])]
    laziki = [__procesuj_linijke_lazikow(
        linijka) for linijka in __wczytaj_pojedynczy_plik(DANE["laziki"])]

    return (obszary, pomiary, laziki)


def __wczytaj_pojedynczy_plik(sciezka):

    tablica = []

    with open(sciezka, "r") as plik:
        index = 0

        for linijka in plik:
            if index == 0:
                index += 1
                continue

            tablica.append(linijka.split("\t"))

    return tablica


def __procesuj_linijke_obszarow(linijka):
    return (linijka[0], linijka[1].rstrip("\n"))


def __procesuj_linijke_pomiarow(linijka):
    rok, miesiac, dzien = linijka[1].split("-")
    return ((int)(linijka[0]), date((int)(rok), (int)(miesiac), (int)(dzien)), linijka[2], linijka[3], (int)(linijka[4]), (int)(linijka[5]))


def __procesuj_linijke_lazikow(linijka):
    return ((int)(linijka[0]), linijka[1], (int)(linijka[2]), linijka[3])


def Rozwiazanie_7_1():
    obszary, pomiary, laziki = __wczytaj_dane()

    kod_max_obszaru = None
    max_woda = 0

    for obszar in obszary:
        kod_obszaru = obszar[0]

        nowa_max_woda = sum([pomiar[5] for pomiar in pomiary if (
            pomiar[4] <= 100 and kod_obszaru == pomiar[2])])

        if nowa_max_woda > max_woda:
            kod_max_obszaru = kod_obszaru
            max_woda = nowa_max_woda

    with open(PLIK_WYNIKOWY, "a") as plik:
        plik.write(
            "7.1 Obszar o najwiekszej ilosci wody na glebokosci do 100 m to: " + [obszar[1] for obszar in obszary if obszar[0] == kod_max_obszaru][0] + "\n")


def Rozwiazanie_7_2():
    obszary, pomiary, laziki = __wczytaj_dane()

    zestawienie = []
    for nr_lazika in [lazik[0] for lazik in laziki]:
        lista_filtr = list(filter(lambda item: item[0] == nr_lazika, laziki))
        nazwa_lazika = lista_filtr[0][1]
        min_data = min([pomiar[1]
                       for pomiar in pomiary if nr_lazika == pomiar[0]])
        max_data = max([pomiar[1]
                       for pomiar in pomiary if nr_lazika == pomiar[0]])
        zestawienie.append({"nazwa_lazika": nazwa_lazika, "pierwszy_dzien": min_data,
                           "ostatni_dzien": max_data, "roznica": (max_data - min_data).days})

    zestawienie.sort(key=lambda wpis: wpis["roznica"], reverse=True)

    with open(PLIK_WYNIKOWY, "a") as plik:
        plik.write(
            "7.2 Nazwa lazika, ktory wykonal pomiary w najdluzszym okresie czasu to: " + zestawienie[0]["nazwa_lazika"] + "\n")
        plik.write(
            "7.2 Pierwszy dzien pomiarow powyzszego lazika to: " + str(zestawienie[0]["pierwszy_dzien"]) + "\n")
        plik.write(
            "7.2 Ostartni dzien pomiarow powyzszego lazika to: " + str(zestawienie[0]["ostatni_dzien"]) + "\n")


def Rozwiazanie_7_3():
    obszary, pomiary, laziki = __wczytaj_dane()

    pomiary_w_roku_lodowania_lazika = []

    for lazik in laziki:
        pomiary_w_roku_lodowania_lazika.extend(
            [pomiar[2] for pomiar in pomiary if pomiar[0] == lazik[0] and pomiar[1].year == lazik[2]])

    with open(PLIK_WYNIKOWY, "a") as plik:
        plik.write(
            "7.3 Obszary, na ktorych nie dylo pomiarow przez zaden lazik w roku ladowania lazika to: ")

        plik.write(", ".join([obszar[1] for obszar in obszary if not obszar[0] in set(
            pomiary_w_roku_lodowania_lazika)]) + "\n")


def Rozwiazanie_7_4():

    obszary, pomiary, laziki = __wczytaj_dane()

    laziki_ktore_wylodowaly_na_poludnowej_polkuli = [
        lazik for lazik in laziki if lazik[3].split(", ")[0][-1] == "S"]

    kody_lazikow_ktore_robily_pomiary_na_poludnowej_polkuli = set(
        [pomiar[0] for pomiar in pomiary if pomiar[3].split(",")[0][-1] == "S"])
    kody_lazikow_ktore_robily_pomiary_na_polnocnej_polkuli = set(
        [pomiar[0] for pomiar in pomiary if pomiar[3].split(",")[0][-1] == "N"])

    laziki = [
        lazik[1] for lazik in laziki_ktore_wylodowaly_na_poludnowej_polkuli if lazik[0] in kody_lazikow_ktore_robily_pomiary_na_poludnowej_polkuli and lazik[0] in kody_lazikow_ktore_robily_pomiary_na_polnocnej_polkuli]

    with open(PLIK_WYNIKOWY, "a") as plik:
        plik.write(
            "7.4 Laziki, ktore wyladowaly na poludniowej polkuli, ale robily pomiary na polnocnej i poludniowej polkuli to: " + ", ".join(laziki))
