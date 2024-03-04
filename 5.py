# 5) Implement a program that reads a text file and counts the occurrences of each word, ignoring case sensitivity.


import re
from collections import Counter

def occurrence(file_name):
    with open(file_name, 'r') as file:
        file_contents = file.read()

    words = re.findall(r'\b\w+\b', file_contents.lower())

    word_counts = Counter(words)

    return word_counts

file_path = 'final.txt'
word_occurrence = occurrence(file_path)

for word, count in word_occurrence.items():
    print(f'{word}: {count} times')
