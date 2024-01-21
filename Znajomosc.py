import networkx as nx
from flask import Flask, jsonify

app = Flask(__name__)

# Dane osobowe
dane_osobowe = {
    'Kamil': {'Znajomi': ['Magda', 'Piotr', 'Daniel'], 'Sprzet': []},
    'Magda': {'Znajomi': ['Kamil', 'Ewa', 'Liliana'], 'Sprzet': ['Kamera']},
    'Ewa': {'Znajomi': ['Magda', 'Liliana', 'Daniel'], 'Sprzet': ['Statyw']},
    'Piotr': {'Znajomi': ['Kamil'], 'Sprzet': []},
    'Nikodem': {'Znajomi': ['Mikołaj'], 'Sprzet': []},
    'Mikołaj': {'Znajomi': ['Nikodem', 'Daniel'], 'Sprzet': []},
    'Liliana': {'Znajomi': ['Magda', 'Ewa'], 'Sprzet': ['Kamera', 'Statyw']},
    'Daniel': {'Znajomi': ['Kamil', 'Ewa', 'Mikołaj'], 'Sprzet': []}
}

# Funkcja znajdująca najkrótszą ścieżkę w grafie
def najkrotsza_sciezka(start, cel, graf):
    if start not in graf or cel not in graf:
        return None
    sciezka = nx.shortest_path(graf, source=start, target=cel)
    return sciezka[1:]  # Zwracamy tylko osoby, nie krawędzie

# Tworzenie grafu
G = nx.Graph()

# Dodawanie wierzchołków
for osoba, dane in dane_osobowe.items():
    G.add_node(osoba)
    for znajomy in dane['Znajomi']:
        G.add_edge(osoba, znajomy)

# API sprawdzające, czy osoby się znają
@app.route('/znajomosc/<osoba1>/<osoba2>', methods=['GET'])
def znajomosc(osoba1, osoba2):
    if osoba1 in dane_osobowe and osoba2 in dane_osobowe:
        return jsonify({"znajomosc": osoba2 in dane_osobowe[osoba1]['Znajomi']})
    else:
        return jsonify({"error": "Osoba nieznana"}), 404

# API zwracające przyjaciół po podaniu imienia
@app.route('/przyjaciele/<osoba>', methods=['GET'])
def przyjaciele(osoba):
    if osoba in dane_osobowe:
        return jsonify({"przyjaciele": dane_osobowe[osoba]['Znajomi']})
    else:
        return jsonify({"error": "Osoba nieznana"}), 404

# API pokazujące ścieżkę - kogo najszybciej zapytać o pożyczenie przedmiotu
@app.route('/sciezka/<osoba>/<przedmiot>', methods=['GET'])
def sciezka(osoba, przedmiot):
    if osoba in dane_osobowe:
        osoby_posiadajace_przedmiot = [os for os in dane_osobowe if przedmiot in dane_osobowe[os]['Sprzet']]
        if not osoby_posiadajace_przedmiot:
            return jsonify({"error": "Przedmiot nie jest dostępny"}), 404
        sciezki = {os: najkrotsza_sciezka(osoba, os, G) for os in osoby_posiadajace_przedmiot}
        najkrotsza = min(sciezki, key=lambda x: len(sciezki[x]))
        return jsonify({"sciezka": sciezki[najkrotsza]})
    else:
        return jsonify({"error": "Osoba nieznana"}), 404

if __name__ == '__main__':
    # Uruchamianie aplikacji Flask
    app.run(debug=True)
