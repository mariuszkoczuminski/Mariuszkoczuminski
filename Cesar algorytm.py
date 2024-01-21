import random
import string
import os

def ceasar_cipher(text, przesuniecie):
    wynik = ""
    for znak in text:
        if znak.isalpha():
            kod_ascii = ord('A') if znak.isupper() else ord('a')
            wynik += chr((ord(znak) - kod_ascii + przesuniecie) % 26 + kod_ascii)
        else:
            wynik += znak
    return wynik

def generator_hasla(dlugosc, duze_litery=True, male_litery=True, cyfry=True, znaki_specjalne=True):
    znaki = ""
    if duze_litery:
        znaki += string.ascii_uppercase
    if male_litery:
        znaki += string.ascii_lowercase
    if cyfry:
        znaki += string.digits
    if znaki_specjalne:
        znaki += string.punctuation

    if not znaki:
        raise ValueError("Przynajmniej jeden rodzaj znaku powinien być dozwolony.")

    return ''.join(random.choice(znaki) for _ in range(dlugosc))

def zapisz_haslo(do_pliku, haslo, przesuniecie):
    zaszyfrowane_haslo = ceasar_cipher(haslo, przesuniecie)
    with open(do_pliku, 'w') as plik:
        plik.write(zaszyfrowane_haslo)


dlugosc_hasla = 25
wygenerowane_haslo = generator_hasla(dlugosc_hasla)

przesuniecie = 9  
plik_zaszyfrowanego_hasla = 'zaszyfrowane_haslo.txt'


sciezka_do_dokumentow = os.path.join(os.path.expanduser("~"), "Documents")
sciezka_do_pliku_zaszyfrowanego_hasla = os.path.join(sciezka_do_dokumentow, plik_zaszyfrowanego_hasla)


zapisz_haslo(sciezka_do_pliku_zaszyfrowanego_hasla, wygenerowane_haslo, przesuniecie)

print("Wygenerowane hasło:", wygenerowane_haslo)
print("Zaszyfrowane hasło zapisane w pliku:", sciezka_do_pliku_zaszyfrowanego_hasla)
