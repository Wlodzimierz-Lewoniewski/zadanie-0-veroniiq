import string
from collections import defaultdict
def sorting_function(lines):
    # Liczba dokumentów
    num_documents = int(lines[0])

    # Pobranie dokumentów
    documents = lines[1:num_documents + 1]

    # Liczba słów do zliczenia
    num_words = int(lines[num_documents + 1])

    # Pobranie słów do zliczenia
    words_to_count = lines[num_documents + 2:num_documents + 2 + num_words]

    # Usunięcie znaków interpunkcyjnych ze słów i zamiana na małe litery
    texts = [[word.strip(string.punctuation) for word in document.lower().split()] for document in documents]

    # Słownik przechowujący licznik wystąpień każdego słowa w każdym dokumencie
    word_counts = defaultdict(list)

    # Zliczanie wystąpień każdego słowa w dokumentach
    for word in words_to_count:
        for doc_id, text in enumerate(texts):
            word_count_in_doc = text.count(word)
            if word_count_in_doc > 0:
                word_counts[word].append((doc_id, word_count_in_doc))

    # Wyniki dla każdego słowa z listy
    results = []

    # Dla każdego słowa sortowanie dokumentów po liczbie wystąpień (malejąco) i zbieranie numerów dokumentów
    for word in words_to_count:
        sorted_docs = sorted(word_counts[word], key=lambda x: (-x[1], x[0]))
        sorted_doc_ids = [doc_id for doc_id, _ in sorted_docs]
        results.append(sorted_doc_ids)

    # Wyświetlanie wyników
    for result in results:
        print(result)

# Odczytywanie zawartości pliku "input.txt"
with open('input2.txt', 'r') as file:
    input_data = file.read()

lines = input_data.strip().split('\n')
sorting_function(lines)