import nltk
from nltk.corpus import wordnet
from translate import Translator

nltk.download('wordnet')
nltk.download('omw-1.4')

def translate_to_polish(text):
    translator = Translator(to_lang="pl")
    translation = translator.translate(text)
    return translation

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

def get_polish_examples(word, max_translations=4):
    examples = []

    synsets = wordnet.synsets(word, lang='pol')

    for syn in synsets:
        for example in syn.examples():
            if len(examples) < max_translations:
                translated_example = translate_to_polish(example)
                if translated_example:
                    examples.append(translated_example)

                    # Sprawdzenie limitów tłumaczeń
                    if 'MYMEMORY WARNING' in translated_example:
                        print("Ostrzeżenie: Przekroczono limit darmowych tłumaczeń. Czekaj na dostępność kolejnych.")
                        time.sleep(60 * 60 * 15)  # Czekaj 15 godzin (czas odnowienia limitu)
            else:
                break

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
        }
        return mapping_pos.get(pos_tag, 'nieznane')
    else:
        return None

def znajdz_synonimy_slowa(slowo):
    synonimy = set()
    for synset in wordnet.synsets(slowo, lang='pol'):
        for lemma in synset.lemmas('pol'):
            synonimy.add(lemma.name())
    return synonimy

def znajdz_antonimy_slowa(slowo):
    antonimy = set()
    for synset in wordnet.synsets(slowo, lang='pol'):
        for lemma in synset.lemmas('pol'):
            if lemma.antonyms():
                antonimy.add(lemma.antonyms()[0].name())
    return antonimy

def main():
    jezyk = input("\nPodaj język ('eng' for English, 'pol' dla Polskiego): ")
    if jezyk not in ['eng', 'pol']:
        print("Błąd: Niepoprawny język. Wybierz 'eng' lub 'pol'.")
        return

    slowo = input("Podaj słowo lub wyrażenie: ")

    synonimy, antonimy = get_synonyms_antonyms(slowo, jezyk)
    polskie_przyklady = get_polish_examples(slowo)
    przyklady = get_examples(slowo, jezyk)
    klasa_gramatyczna = classify_word(slowo, jezyk)
    pelna_nazwa_klasy = get_full_class_name(slowo, jezyk)

    synonimy_pol = znajdz_synonimy_slowa(slowo)
    antonimy_pol = znajdz_antonimy_slowa(slowo)

    print("\nSynonimy:", synonimy_pol if jezyk == 'pol' else synonimy)
    print("Antonimy:", antonimy_pol if jezyk == 'pol' else antonimy)
    print("Przykłady użycia:", polskie_przyklady if jezyk == 'pol' else przyklady)
    print("Klasa gramatyczna:", pelna_nazwa_klasy)

if __name__ == "__main__":
    main()
