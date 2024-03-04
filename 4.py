# 4) Merge Multiple Text Files into One


file_names = ['new.txt', 'first.txt', 'initial.txt']

final_file_name = 'final.txt'

with open(final_file_name, 'w') as output_file:

    for file_path in file_names:
        with open(file_path, 'r') as input_file:
            file_contents = input_file.read()

            output_file.write(file_contents)

print(f'Merged files into {final_file_name}')
