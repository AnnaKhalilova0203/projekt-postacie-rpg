
"""Pierwsza wersja systemu porównywania postaci RPG z NumPy."""
import csv
import numpy as np

# Nazwy postaci
NAZWY = np.array([
    "Wojownik",
    "Mag",
    "Łucznik",
    "Paladyn",
    "Łotrzyk",
    "Berserker",
    "Druid",
    "Strażnik"
])

# Statystyki: HP, atak, obrona, szybkość
STATYSTYKI = np.array([
    [120, 28, 18, 9],
    [75, 44, 6, 13],
    [95, 34, 10, 17],
    [140, 25, 22, 7],
    [80, 39, 8, 21],
    [110, 42, 7, 12],
    [105, 26, 15, 14],
    [155, 18, 26, 5]
], dtype=float)

# Nazwy kolumn
KOLUMNY = ("HP", "Atak", "Obrona", "Szybkość")

# Sprawdzenie struktury danych
print("Liczba postaci:", len(NAZWY))
print("Wymiary macierzy:", STATYSTYKI.shape)
print("Typ danych:", STATYSTYKI.dtype)
print("Kolumny:", KOLUMNY)




WAGI = np.array([0.20, 0.40, 0.25, 0.15])


def normalizuj(dane):
    minimum = np.min(dane, axis=0)
    maksimum = np.max(dane, axis=0)
    rozpietosc = maksimum - minimum

    return np.divide(
        dane - minimum,
        rozpietosc,
        out=np.zeros_like(dane, dtype=float),
        where=rozpietosc != 0
    )


def oblicz_sile(dane):
    dane_norm = normalizuj(dane)
    return dane_norm @ WAGI


sily = oblicz_sile(STATYSTYKI)

print("\n=== SIŁA POSTACI ===")

for nazwa, sila in zip(NAZWY, sily):
    print(f"{nazwa}: {sila:.4f}")
def waliduj(nazwy, dane):
    if dane.ndim != 2:
        raise ValueError("Dane muszą być macierzą 2D.")

    if dane.shape != (len(nazwy), 4):
        raise ValueError("Nieprawidłowy rozmiar macierzy.")

    if len(nazwy) < 2:
        raise ValueError("Muszą istnieć co najmniej dwie postacie.")

    if len(set(nazwy)) != len(nazwy):
        raise ValueError("Nazwy postaci muszą być unikalne.")

    if not np.issubdtype(dane.dtype, np.number):
        raise ValueError("Statystyki muszą być liczbami.")

    if not np.all(np.isfinite(dane)):
        raise ValueError("Dane muszą być wartościami skończonymi.")

    if np.any(dane < 0):
        raise ValueError("Statystyki nie mogą być ujemne.")

    return True


print("\n=== WALIDACJA DANYCH ===")
waliduj(NAZWY, STATYSTYKI)
print("Dane są poprawne!")
def okresl_role(dane):
    hp = dane[:, 0]
    atak = dane[:, 1]
    obrona = dane[:, 2]
    szybkosc = dane[:, 3]

    ofensywa = (atak >= 35) & (szybkosc >= 12)
    defensywa = (hp >= 120) & (obrona >= 18)

    return np.select(
        [ofensywa, defensywa],
        ["Szturmowiec", "Obrońca"],
        default="Wszechstronny"
    )


role = okresl_role(STATYSTYKI)

print("\n=== ROLE POSTACI ===")

for nazwa, rola in zip(NAZWY, role):
    print(f"{nazwa}: {rola}")
    # Ranking postaci
ranking = np.argsort(-sily, kind="stable")

print("\n=== RANKING POSTACI ===")

for miejsce, indeks in enumerate(ranking, start=1):
    print(
        f"{miejsce}. {NAZWY[indeks]} | "
        f"Rola: {role[indeks]} | "
        f"Siła: {sily[indeks]:.3f}"
    )

# Filtrowanie postaci
maska = (
    (STATYSTYKI[:, 0] >= 100)
    & (STATYSTYKI[:, 3] >= 10)
    & (sily >= 0.45)
)

print("\n=== POSTACIE SPEŁNIAJĄCE WARUNKI ===")

for nazwa in NAZWY[maska]:
    print(nazwa)


# Statystyki grupy
print("\n=== STATYSTYKI GRUPY ===")

for i, kolumna in enumerate(KOLUMNY):
    wartosci = STATYSTYKI[:, i]

    print(
        f"{kolumna:<10}: "
        f"min={np.min(wartosci):.1f}, "
        f"średnia={np.mean(wartosci):.1f}, "
        f"max={np.max(wartosci):.1f}"
    )

def macierz_pojedynkow(sila):
    roznice = sila[:, np.newaxis] - sila[np.newaxis, :]
    prawdopodobienstwo = 1 / (1 + np.exp(-8 * roznice))

    np.fill_diagonal(prawdopodobienstwo, 0.5)

    return prawdopodobienstwo


pojedynki = macierz_pojedynkow(sily)

srednie_szanse = (
    pojedynki.sum(axis=1) - 0.5
) / (len(NAZWY) - 1)

print("\n=== ŚREDNIE SZANSE WYGRANEJ ===")

for nazwa, szansa in zip(NAZWY, srednie_szanse):
    print(f"{nazwa}: {szansa:.1%}")
def testy():
    # Test normalizacji stałej kolumny
    dane_stale = np.array([
        [10, 1],
        [10, 2],
        [10, 3]
    ], dtype=float)

    wynik = normalizuj(dane_stale)

    assert np.all(wynik[:, 0] == 0), \
        "Kolumna stała powinna zawierać same zera."

    assert np.allclose(wynik[:, 1], [0, 0.5, 1]), \
        "Niepoprawna normalizacja."

    # Test macierzy pojedynków
    test_sily = np.array([0.2, 0.5, 0.8])
    macierz = macierz_pojedynkow(test_sily)

    assert np.allclose(np.diag(macierz), 0.5), \
        "Przekątna macierzy powinna wynosić 0.5."

    assert np.allclose(macierz + macierz.T, 1.0), \
        "Prawdopodobieństwa powinny sumować się do 1."

    print("Wszystkie testy zakończone pomyślnie!")


print("\n=== TESTY ===")
testy()
def zapisz_csv(nazwy, role, sily, szanse, ranking):
    with open(
        "raport_postaci.csv",
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as plik:

        writer = csv.writer(plik, delimiter=";")

        writer.writerow([
            "Miejsce",
            "Postać",
            "Rola",
            "Siła",
            "Średnia szansa wygranej"
        ])

        for miejsce, indeks in enumerate(ranking, start=1):
            writer.writerow([
                miejsce,
                nazwy[indeks],
                role[indeks],
                f"{sily[indeks]:.4f}",
                f"{szanse[indeks]:.2%}"
            ])


zapisz_csv(NAZWY, role, sily, srednie_szanse, ranking)

print("\nRaport zapisano do pliku raport_postaci.csv")