# 6) Write a Python function that takes a list of strings as input and returns a new list with the strings sorted in descending order of their lengths.

def sort_strings_by_length(strings):
    sorted_strings = sorted(strings, key=len, reverse=True)
    return sorted_strings

input_strings = input("Enter a list of strings separated by space: ")
input_list = input_strings.split()
result = sort_strings_by_length(input_list)

print(result)

