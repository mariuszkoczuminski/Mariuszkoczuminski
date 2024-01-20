
import heapq

def dij(graph, start):
    # Inicjalizacjemy odleglość i kolejki
    odleglosci = {wierzcholek: float('infinity') for wierzcholek in graph}
    odleglosci[start] = 0
    kolejka_priorytetowa = [(0, start)]

    while kolejka_priorytetowa:
        aktualna_odleglosc, aktualny_wierzcholek = heapq.heappop(kolejka_priorytetowa)

        # Jeśli już znaleźliśmy krótszą ścieżkę do danego wierzchołka, pomijamy go
        if aktualna_odleglosc > odleglosci[aktualny_wierzcholek]:
            continue

        # Badamy sąsiadów
        for sasiad, waga in graph[aktualny_wierzcholek].items():
            odleglosc = aktualna_odleglosc + waga

            # Jeśli znaleziono krótszą ścieżkę, aktualizujemy odległość i dodajemy do kolejki
            if odleglosc < odleglosci[sasiad]:
                odleglosci[sasiad] = odleglosc
                heapq.heappush(kolejka_priorytetowa, (odleglosc, sasiad))

    return odleglosci


graf = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 3, 'E': 3, 'D': 2,'A': 100},
    'C': {'E': 5, 'B': 1, 'D': 4},
    'D': {'B': 100, 'C': 100, 'E': 100},
    'E': {'B':100, 'C': 100, 'D': 1},
}

startowy_wierzcholek = 'A'
wynik = dij(graf, startowy_wierzcholek)

print(f"Najkrótsze odległości od {startowy_wierzcholek}:")
for wierzcholek, odleglosc in wynik.items():
    print(f"Do {wierzcholek}: {odleglosc}")
