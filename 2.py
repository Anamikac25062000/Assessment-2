# 2) Count the Number of Lines, Words, and Characters in a Text File


file_name = 'new.txt'
with open(file_name, 'r') as file:
    file_lines = file.readlines()

num_lines = len(file_lines)

num_words = sum(len(line.split()) for line in file_lines)
num_char = sum(len(line) for line in file_lines)

# Print the results
print(f"Number of lines: {num_lines}")
print(f"Number of words: {num_words}")
print(f"Number of characters: {num_char}")
