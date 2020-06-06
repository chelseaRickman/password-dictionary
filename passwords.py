from itertools import permutations

def generate_passwords(keywords, number_of_words):
    return list(permutations(keywords, number_of_words))

def print_passwords_to_file(combinations):
    with open("target_dictionary.txt", "a") as dictionary_file:
        dictionary_entry = ""
        for combo in combinations:
            for j in combo:
                dictionary_entry += j
            dictionary_file.write(dictionary_entry + '\n')
            dictionary_entry = ""

