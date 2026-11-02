# Projekt: Porównywanie postaci RPG

## 1. Cel projektu

Celem projektu było przekształcenie programu porównującego postacie RPG z wersji A do wersji B. Wersja wynikowa wykorzystuje bibliotekę NumPy do przechowywania danych, normalizacji statystyk, obliczania siły postaci i analizy pojedynków.

## 2. Wprowadzone funkcjonalności

W programie wynikowym zaimplementowano:

- przechowywanie statystyk postaci w macierzy NumPy;
- normalizację min-max z obsługą kolumn o stałej wartości;
- obliczanie siły postaci na podstawie wag;
- walidację danych wejściowych;
- automatyczne określanie ról postaci;
- ranking postaci według siły;
- filtrowanie postaci według określonych warunków;
- obliczanie statystyk grupy;
- macierz prawdopodobieństw pojedynków;
- obliczanie średnich szans wygranej;
- testy automatyczne;
- eksport wyników do pliku CSV.

## 3. Wyniki testowania

Program został uruchomiony w Pythonie 3.12.0. Testy automatyczne zakończyły się komunikatem:

`Wszystkie testy zakończone pomyślnie!`

Ranking rozpoczyna się od postaci Berserker, a na ostatnim miejscu znajduje się Druid. Program poprawnie wygenerował plik `raport_postaci.csv`.

## 4. Porównanie z wersją B

Wyniki rankingu, role postaci, siła oraz średnie szanse wygranej są zgodne z wersją B. Po dodatkowej poprawce program wyświetla również statystyki HP, Atak, Obrona i Szybkość dla całej grupy.

Plik CSV zawiera osiem postaci i pięć kolumn. Dane zapisano z separatorem średnika.

## 5. Pliki projektu

- `01_kod_poczatkowy.py` — oryginalna wersja A;
- `02_kod_docelowy.py` — wersja B;
- `03_kod_wynikowy.py` — program wynikowy;
- `prompty.md` — zestaw instrukcji użytych do planowania zmian;
- `testy_i_poprawki.md` — tabela testów i opis poprawek;
- `raport_postaci.csv` — raport wygenerowany przez program.

## 6. Wnioski

Podczas realizacji projektu wykorzystano bibliotekę NumPy do wykonywania operacji na macierzach i wektorach. Dodano walidację danych, testy automatyczne oraz eksport wyników do CSV. Porównanie z wersją B potwierdziło zgodność najważniejszych obliczeń i wyników programu.

