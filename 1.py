# 1) Read and Print the Contents of a Text File


file_name = 'new.txt'
with open(file_name, 'r') as file:
    contents = file.read()

print(contents)
