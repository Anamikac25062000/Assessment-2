# 16) Count the total number of uppercase characters in a file in Python


def count_upper_char(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            uppercase_count = sum(1 for char in content if char.isupper())
            return uppercase_count
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"Error: {e}")

file_name = '1.txt'
result = count_upper_char(file_name)

if result is not None:
    print(f"Total number of uppercase characters in '{file_name}': {result}")

