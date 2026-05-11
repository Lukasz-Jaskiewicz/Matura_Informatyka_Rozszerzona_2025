-- Zadanie 7.1
SELECT nazwa_obszaru FROM obszary o INNER JOIN( 
		SELECT kod_obszaru, SUM(ilosc) AS ilosci FROM pomiary WHERE glebokosc <= 100 GROUP BY kod_obszaru
	) one ON o.kod_obszaru = one.kod_obszaru WHERE ilosci = (
		SELECT MAX(sumy) as ilosci FROM (
			SELECT SUM(ilosc) AS sumy FROM pomiary WHERE glebokosc <= 100 GROUP BY kod_obszaru
		) as zero
	);
-- Zadanie 7.2
-- Dla lazika, ktory wykonal pomiary w najdluzszym okresie
SELECT nazwa_lazika, czestosci FROM (
		SELECT nr_lazika, COUNT(*) czestosci FROM pomiary GROUP BY nr_lazika
	) as zestawienie_czestosci INNER JOIN laziki l ON zestawienie_czestosci.nr_lazika = l.nr_lazika
	WHERE czestosci =(
			SELECT MAX(czestosci) FROM (
				SELECT COUNT(*) AS czestosci FROM pomiary GROUP BY nr_lazika
			) as max_czestosc
	);

-- dla lazika, ktory wykonal pierwszy i ostatni pomiar
SELECT nazwa_lazika, MIN(data_pomiaru) AS pierwszy_pomiar, MAX(data_pomiaru) AS ostatni_pomiar FROM pomiary p INNER JOIN laziki l ON p.nr_lazika = l.nr_lazika WHERE p.nr_lazika = (
	SELECT nr_lazika FROM (
			SELECT p.nr_lazika, nazwa_lazika, COUNT(*) czestosci FROM pomiary p INNER JOIN laziki l ON p.nr_lazika = l.nr_lazika GROUP BY p.nr_lazika
		) as zestawienie_czestosci 
	WHERE czestosci =(
			SELECT MAX(czestosci) FROM (
				SELECT COUNT(*) AS czestosci FROM pomiary GROUP BY nr_lazika
			) as max_czestosc
		)
	) GROUP BY p.nr_lazika;

-- Zadanie 7.3
SELECT DISTINCT nazwa_obszaru FROM obszary WHERE kod_obszaru NOT IN (
    SELECT DISTINCT p.kod_obszaru FROM pomiary p INNER JOIN laziki l ON p.nr_lazika = l.nr_lazika WHERE YEAR(data_pomiaru) = l.rok_wyslania
);

--Zadanie 7.4
SELECT DISTINCT l.nazwa_lazika FROM pomiary p INNER JOIN laziki l ON p.nr_lazika = l.nr_lazika WHERE 
	l.wsp_lodowania LIKE "%S%" AND
	l.nr_lazika IN (
		SELECT nr_lazika FROM pomiary WHERE wspolrzedne LIKE "%S%"
	) AND 
    l.nr_lazika IN (
		SELECT nr_lazika FROM pomiary WHERE wspolrzedne LIKE "%N%"
	);