# 15) Copy odd lines of one file to another file in Python


def odd_lines(input_file, output_file):
    with open(input_file, 'r') as input_f, open(output_file, 'w') as output_f:
        lines = input_f.readlines()
        odd_lines = [line for idx, line in enumerate(lines, 1) if idx % 2 != 0]
        output_f.writelines(odd_lines)

input_filename = "1.txt"
output_filename = "2.txt"
odd_lines(input_filename, output_filename)
