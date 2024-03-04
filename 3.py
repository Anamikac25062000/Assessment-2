# 3) Search for a String in a Text File


file_name = 'new.txt'
string_in_file =input("Enter the string you want: ")

with open(file_name, 'r') as file:
    for line_num, line in enumerate(file, start=1):
        if string_in_file in line:
            print(f"Found '{string_in_file}' in line {line_num}:")
            print(line)

