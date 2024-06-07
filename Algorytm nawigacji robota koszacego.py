class RobotKoszacy:
    def __init__(self, szerokosc, wysokosc):
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.x = 0
        self.y = 0
        self.kierunek = 1  # 1 oznacza w prawo, -1 oznacza w lewo
        self.teren = [[False for _ in range(szerokosc)] for _ in range(wysokosc)]

    def koszenie(self):
        while not self.czy_skonczone():
            self.kos()
            self.przesun()

    def kos(self):
        self.teren[self.y][self.x] = True
        print(f'Koszenie pozycji: ({self.x}, {self.y})')

    def przesun(self):
        if self.kierunek == 1:
            if self.x < self.szerokosc - 1:
                self.x += 1
            else:
                self.y += 1
                self.kierunek = -1
        else:
            if self.x > 0:
                self.x -= 1
            else:
                self.y += 1
                self.kierunek = 1

    def czy_skonczone(self):
        return all(all(wiersz) for wiersz in self.teren)

# Przykład użycia
robot = RobotKoszacy(5, 4)
robot.koszenie()
