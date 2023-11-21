import json
import time

# Ścieżka dostępu do pliku (może to być ścieżka względna lub bezwzględna)
sciezka = r"C:\Users\Kmari\Desktop\imiona.json"

# otwieranie pliku imiona.json
with open(sciezka, "r") as file:
    data = json.load(file)

# przetwarzanie słownika w z json na lista PYTHON
nowa_lista = list()
for w in data['data']:
    nowa_lista.append(w[11])

# podanie imienia i wyszukiwanie 
poziom = 0
szukane_imie = input("Podaj szukane imie:")
start = time.time()
for w in data['data']:
    poziom += 1
    if w[11] == szukane_imie.upper():
        print()
        print(w, f'\nIle razy powtarza sie imie : {poziom}')
        print()
        break
end = time.time()
print()
koniec_pomiaru = end - start
print('Czas wyszukiwania imienia w Json w s', koniec_pomiaru)