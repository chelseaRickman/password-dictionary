import re
from passwords import *

file_name = input("Enter the name of the text file (including the file extension) containing the key words for the target: ")

keywords = []
with open(file_name, "r") as keyword_file:
    for line in keyword_file:
        stripped_line = line.strip()
        multiple_words = re.split('[ \./]', stripped_line)
        for i in range(0, len(multiple_words)):
            keywords.append(multiple_words[i].lower())

for i in range(2, 5):
    combinations = generate_passwords(keywords, i)
    print_passwords_to_file(combinations)









