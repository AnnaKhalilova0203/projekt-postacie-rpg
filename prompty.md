# Prompty do przekształcenia programu RPG --- wersja A do wersji B

## Cel zadania

Celem jest stopniowe przekształcenie programu porównującego postacie RPG
z wersji A do programu o funkcjonalności zgodnej z wersją B. Model
powinien otrzymać kod wersji A, a następnie realizować kolejne
polecenia. Nie należy wklejać modelowi kodu wersji B --- wersja B służy
wyłącznie do późniejszego porównania wyników.

> Uwaga organizacyjna: prompty poniżej są przygotowaną sekwencją
> instrukcji. W sprawozdaniu należy opisać tylko te prompty i poprawki,
> które rzeczywiście zostały użyte podczas pracy. Nie należy twierdzić,
> że przeprowadzono eksperyment w nowej rozmowie, jeśli tak się nie
> stało.

## Prompt 1. Analiza kodu i przygotowanie danych w NumPy

Przeanalizuj otrzymany kod wersji A. Przepisz dane postaci do tablic
NumPy: osobnej tablicy nazw oraz dwuwymiarowej macierzy statystyk.
Zachowaj kolejność postaci i kolejność cech: HP, Atak, Obrona, Szybkość.
Macierz statystyk ma mieć typ liczbowy zmiennoprzecinkowy. Na tym etapie
nie dodawaj jeszcze rankingu ani dodatkowych funkcji. Pokaż kompletny
kod po zmianie.

**Oczekiwana zmiana:** dane zapisane w tablicach NumPy zamiast listy
słowników.

## Prompt 2. Normalizacja i obliczanie siły

Dodaj normalizację min-max każdej kolumny macierzy statystyk. Zabezpiecz
działanie dla kolumny, w której wszystkie wartości są takie same ---
taka kolumna po normalizacji ma zawierać zera, bez dzielenia przez zero.
Następnie oblicz siłę postaci jako iloczyn znormalizowanej macierzy i
wektora wag `[0.20, 0.40, 0.25, 0.15]`. Wyświetl siłę każdej postaci z
dokładnością do czterech miejsc po przecinku. Pokaż kompletny kod.

**Oczekiwana zmiana:** normalizacja min-max i ważona ocena siły.

## Prompt 3. Walidacja danych

Dodaj funkcję `waliduj(nazwy, dane)`. Funkcja ma sprawdzać, czy dane są
macierzą dwuwymiarową z czterema kolumnami, czy liczba wierszy odpowiada
liczbie nazw, czy są co najmniej dwie postacie, czy nazwy są unikalne
oraz czy wszystkie wartości statystyk są liczbowe, skończone i
nieujemne. W przypadku niepoprawnych danych zgłoś czytelny `ValueError`.
Wywołaj walidację przed dalszymi obliczeniami. Pokaż kompletny kod.

**Oczekiwana zmiana:** kontrola poprawności danych przed obliczeniami.

## Prompt 4. Automatyczne określanie ról

Dodaj funkcję `okresl_role(dane)`. Postać ma otrzymać rolę
`Szturmowiec`, jeśli Atak jest większy lub równy 35 i Szybkość jest
większa lub równa 12. W przeciwnym razie ma otrzymać rolę `Obrońca`,
jeśli HP jest większe lub równe 120 i Obrona jest większa lub równa 18.
Pozostałe postacie otrzymują rolę `Wszechstronny`. Jeśli postać spełnia
oba zestawy warunków, pierwszeństwo ma `Szturmowiec`. Wyświetl role
wszystkich postaci. Pokaż kompletny kod.

**Oczekiwana zmiana:** klasyfikacja postaci na podstawie statystyk.

## Prompt 5. Ranking, filtrowanie i statystyki grupy

Dodaj ranking postaci według siły --- od największej do najmniejszej.
Przy sortowaniu zachowaj stabilną kolejność dla remisów. Wyświetl
miejsce, nazwę, rolę i siłę. Następnie wybierz postacie spełniające
jednocześnie warunki: HP \>= 100, Szybkość \>= 10 oraz siła \>= 0.45.
Wyświetl wybrane postacie. Oblicz minimum, średnią i maksimum dla każdej
z czterech cech w całej grupie. Pokaż kompletny kod.

**Oczekiwana zmiana:** ranking, filtrowanie i statystyki opisowe
czterech cech.

## Prompt 6. Macierz pojedynków i średnie szanse wygranej

Dodaj funkcję `macierz_pojedynkow(sila)`. Oblicz różnice siły pomiędzy
każdą parą postaci z użyciem broadcastingu NumPy, a następnie
przekształć je na prawdopodobieństwo za pomocą funkcji logistycznej
`1 / (1 + exp(-8 * różnica))`. Na przekątnej macierzy ustaw wartość 0.5.
Oblicz średnią szansę wygranej każdej postaci, pomijając pojedynek z
samą sobą. Wyświetl wyniki jako procenty. Pokaż kompletny kod.

**Oczekiwana zmiana:** macierz prawdopodobieństw pojedynków i średnie
szanse wygranej.

## Prompt 7. Testy automatyczne

Dodaj funkcję `testy()`. Sprawdź co najmniej: normalizację kolumny o
stałej wartości (wynik powinien zawierać same zera), normalizację
kolumny zmiennej (minimum 0, maksimum 1), wartości 0.5 na przekątnej
macierzy pojedynków oraz zależność, że prawdopodobieństwa dla
przeciwnych kierunków pojedynku sumują się do 1. Wywołaj testy podczas
uruchamiania programu i wyświetl komunikat o pomyślnym zakończeniu.
Upewnij się, że wywołanie testów znajduje się poza definicją funkcji.
Pokaż kompletny kod.

**Oczekiwana zmiana:** automatyczne testowanie kluczowych własności
obliczeń.

## Prompt 8. Eksport CSV i uporządkowanie programu

Dodaj eksport wyników do pliku `raport_postaci.csv`. Użyj modułu `csv`,
kodowania `utf-8-sig`, `newline=""` i separatora średnika. Nagłówki mają
być następujące: `Miejsce`, `Postać`, `Rola`, `Siła`,
`Średnia szansa wygranej`. Zapisuj postacie w kolejności rankingu, siłę
z czterema miejscami po przecinku, a szansę jako procent z dwoma
miejscami po przecinku. Uporządkuj program tak, aby po uruchomieniu
wykonywał walidację, testy, obliczenia, wyświetlanie wyników i zapis
CSV. Pokaż kompletny kod wynikowy.

**Oczekiwana zmiana:** zapis raportu CSV i uporządkowany przebieg
programu.

## Dodatkowe prompty korygujące --- używać tylko wtedy, gdy pojawi się dany problem

### Korekta A. Kolumna o stałej wartości

W normalizacji min-max zabezpiecz dzielenie przez zero. Użyj `np.divide`
z tablicą wynikową wypełnioną zerami i warunkiem
`where=rozpietosc != 0`, tak aby kolumna o zerowym zakresie została
znormalizowana do samych zer. Pokaż poprawioną funkcję normalizacji.

### Korekta B. Przekątna i średnia szansa wygranej

Upewnij się, że przekątna macierzy pojedynków ma wartość 0.5. Przy
obliczaniu średniej szansy wygranej odejmij 0.5 od sumy wiersza, a
następnie podziel przez liczbę pozostałych przeciwników, czyli
`len(nazwy) - 1`. Pokaż poprawiony fragment kodu.

### Korekta C. Wcięcia w funkcji

Jeśli pojawi się `IndentationError`, zwróć cały poprawiony blok funkcji,
a nie pojedyncze linie. Każda instrukcja wewnątrz funkcji ma być wcięta
o cztery spacje. Nie zmieniaj pozostałej logiki programu.

### Korekta D. Oddzielenie plików

Nie nadpisuj pliku źródłowego A ani pliku docelowego B. Oryginalny kod A
zachowaj w `01_kod_poczatkowy.py`, kod B w `02_kod_docelowy.py`, a
program wynikowy zapisuj w `03_kod_wynikowy.py`.

## Lista kontrolna po wygenerowaniu programu

-   [ ] Kod A pozostał zachowany bez zmian.
-   [ ] Kod B pozostał zachowany bez zmian.
-   [ ] Kod wynikowy znajduje się w osobnym pliku.
-   [ ] Macierz statystyk ma 8 wierszy i 4 kolumny.
-   [ ] Normalizacja obsługuje kolumnę o stałej wartości.
-   [ ] Walidacja danych działa.
-   [ ] Role i ranking są poprawne.
-   [ ] Filtrowanie wybiera właściwe postacie.
-   [ ] Statystyki grupy obejmują HP, Atak, Obronę i Szybkość.
-   [ ] Testy automatyczne przechodzą pomyślnie.
-   [ ] Plik CSV zawiera nagłówki i 8 rekordów.
-   [ ] Wyniki programu porównano z wersją B.
