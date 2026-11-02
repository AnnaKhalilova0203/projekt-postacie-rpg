# Testy i weryfikacja programu

## 1. Tabela zgodności wymagań

| Wymaganie | Status | Dowód lub wynik testu |
|---|---|---|
| Reprezentacja postaci w macierzy NumPy | Działa | Macierz ma rozmiar (8, 4), typ float64 |
| Normalizacja min-max | Działa | Wyniki siły zgodne z oczekiwanymi wartościami |
| Obsługa kolumny o stałej wartości | Działa | Test potwierdził, że znormalizowana kolumna zawiera zera |
| Obliczanie siły z użyciem wag | Działa | Berserker: 0.5349, Łotrzyk: 0.5106 |
| Walidacja danych | Działa | Komunikat „Dane są poprawne!” |
| Określanie ról postaci | Działa | Wszystkie 8 ról wyświetlono prawidłowo |
| Ranking malejący | Działa | Berserker zajmuje 1. miejsce, Druid 8. miejsce |
| Filtrowanie postaci | Działa | Wybrano Berserkera |
| Statystyki wybranej grupy | Działa | Minimum, średnia i maksimum: 0.5349 |
| Macierz pojedynków | Działa | Przekątna wynosi 0.5, prawdopodobieństwa są symetryczne do 1 |
| Średnie szanse wygranej | Działa | Berserker: 63.98%, Druid: 33.53% |
| Testy automatyczne | Działa | „Wszystkie testy zakończone pomyślnie!” |
| Eksport CSV | Działa | 8 rekordów, 5 kolumn, separator średnikowy |
| Formatowanie raportu CSV | Działa | Siła: 4 miejsca po przecinku; szansa: 2 miejsca procentowe |

## 2. Rzeczywiste poprawki instrukcji

### Poprawka 1 — nieprawidłowe wcięcie w funkcji

**Problem:** Po dodaniu funkcji `macierz_pojedynkow()` program zwrócił błąd `IndentationError`.

**Przyczyna:** Instrukcje wewnątrz funkcji nie miały prawidłowego wcięcia.

**Poprawiona instrukcja:**

„Popraw funkcję `macierz_pojedynkow()`. Każda instrukcja należąca do funkcji musi być wcięta o 4 spacje. Zwróć kompletny poprawiony fragment kodu, zachowując pozostałą logikę programu”.

**Wynik:** Po poprawieniu wcięć program uruchomił się prawidłowo.

### Poprawka 2 — ochrona oryginalnego pliku

**Problem:** Pierwsze instrukcje prowadziły do modyfikowania pliku `01_kod_poczatkowy.py`, który powinien zachować oryginalną wersję A.

**Przyczyna:** Nie określono wystarczająco jasno, w którym pliku należy zapisywać kod wynikowy.

**Poprawiona instrukcja:**

„Nie modyfikuj pliku źródłowego A ani pliku docelowego B. Zachowaj oba pliki bez zmian. Cały wygenerowany program zapisuj w osobnym pliku `03_kod_wynikowy.py`. Oryginalny plik A musi pozostać dostępny do porównania”.

**Wynik:** Oryginalny kod A został przywrócony, kod wynikowy zapisano w osobnym pliku `03_kod_wynikowy.py`.

## 3. Podsumowanie testów

Program `03_kod_wynikowy.py` został uruchomiony w środowisku Python 3.12.0. Wszystkie testy automatyczne zakończyły się pomyślnie. Wygenerowano również plik `raport_postaci.csv`.

Wyniki rankingu, role postaci, filtrowanie oraz wartości siły i średnich szans wygranej są zgodne z oczekiwanymi wynikami wersji docelowej B.
