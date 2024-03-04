# 17) Python program to delay printing of line from a file using sleep function


import time

def print_lines_with_delay(file_path, delay_seconds):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip())
                time.sleep(delay_seconds)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

file_path = '1.txt'
delay_seconds = 3 

print_lines_with_delay(file_path, delay_seconds)

