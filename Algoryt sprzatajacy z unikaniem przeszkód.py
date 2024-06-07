import heapq

class RobotSprzatajacy:
    def __init__(self, szerokosc, wysokosc, przeszkody, obszar_sprzatania):
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.x = 0
        self.y = 0
        self.teren = [[False for _ in range(szerokosc)] for _ in range(wysokosc)]
        self.przeszkody = przeszkody
        self.obszar_sprzatania = obszar_sprzatania

    def sprzatanie(self):
        while not self.czy_skonczone():
            if (self.x, self.y) in self.obszar_sprzatania and not self.jest_przeszkoda(self.x, self.y):
                self.sprzataj()
            self.przesun()

    def sprzataj(self):
        self.teren[self.y][self.x] = True
        print(f'Sprzątanie pozycji: ({self.x}, {self.y})')

    def przesun(self):
        nastepna_pozycja = self.znajdz_nastepna_pozycja()
        if nastepna_pozycja:
            self.x, self.y = nastepna_pozycja

    def znajdz_nastepna_pozycja(self):
        sasiedzi = [(self.x + 1, self.y), (self.x - 1, self.y), (self.x, self.y + 1), (self.x, self.y - 1)]
        sasiedzi = [(x, y) for x, y in sasiedzi if self.w_zakresie(x, y) and not self.teren[y][x] and not self.jest_przeszkoda(x, y)]
        
        if not sasiedzi:
            return None
        
        # Heurystyka do wyboru sąsiedniej pozycji (np. najbliżej lewego górnego rogu)
        sasiedzi.sort(key=lambda pos: (pos[1], pos[0]))
        return sasiedzi[0]

    def jest_przeszkoda(self, x, y):
        return (x, y) in self.przeszkody

    def w_zakresie(self, x, y):
        return 0 <= x < self.szerokosc and 0 <= y < self.wysokosc

    def czy_skonczone(self):
        for y in range(self.wysokosc):
            for x in range(self.szerokosc):
                if (x, y) in self.obszar_sprzatania and not self.teren[y][x] and not self.jest_przeszkoda(x, y):
                    return False
        return True

# Przykład użycia
przeszkody = {(2, 1), (3, 2)}
obszar_sprzatania = {(x, y) for x in range(5) for y in range(4)}  # Zaznaczony obszar do sprzątania
robot = RobotSprzatajacy(5, 4, przeszkody, obszar_sprzatania)
robot.sprzatanie()
