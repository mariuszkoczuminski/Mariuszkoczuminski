import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import wordnet

def get_synonyms_antonyms(word, lang='eng'):
    synonyms = []
    antonyms = []

    if lang == 'eng':
        synsets = wordnet.synsets(word, lang='eng')
    elif lang == 'pol':
        synsets = wordnet.synsets(word, lang='pol')
    else:
        return set(), set()

    for syn in synsets:
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
            if lemma.antonyms():
                antonyms.append(lemma.antonyms()[0].name())

    return set(synonyms), set(antonyms)

def get_examples(word, lang='eng'):
    examples = []

    if lang == 'eng':
        synsets = wordnet.synsets(word, lang='eng')
    elif lang == 'pol':
        synsets = wordnet.synsets(word, lang='pol')
    else:
        return examples

    for syn in synsets:
        examples.extend(syn.examples())

    return examples

def classify_word(word, lang='eng'):
    if lang == 'eng':
        synsets = wordnet.synsets(word, lang='eng')
    elif lang == 'pol':
        synsets = wordnet.synsets(word, lang='pol')
    else:
        return None

    if synsets:
        return synsets[0].pos()
    else:
        return None

def get_full_class_name(word, lang='eng'):
    if lang == 'eng':
        synsets = wordnet.synsets(word, lang='eng')
    elif lang == 'pol':
        synsets = wordnet.synsets(word, lang='pol')
    else:
        return None

    if synsets:
        pos_tag = synsets[0].pos()
        mapping_pos = {
            'n': 'rzeczownik',
            'v': 'czasownik',
            'r': 'przysłówek',
            'a': 'przymiotnik'
            # Jesli potrzebne beda inne kategorie proszę dodać
        }
        return mapping_pos.get(pos_tag, 'nieznane')
    else:
        return None

def main():
    
    jezyk = input("Podaj język ('eng' dla angielskiego, 'pol' dla polskiego): ")
    slowo = input("Podaj słowo lub wyrażenie: ")

    synonimy, antonimy = get_synonyms_antonyms(slowo, jezyk)
    przyklady = get_examples(slowo, jezyk)
    klasa_gramatyczna = classify_word(slowo, jezyk)
    pelna_nazwa_klasy = get_full_class_name(slowo, jezyk)

    print("\nSynonimy:", synonimy)
    print("Antonimy:", antonimy)
    print("Przykłady użycia:", przyklady)
    print("Klasa gramatyczna:", pelna_nazwa_klasy)

if __name__ == "__main__":
    main()
