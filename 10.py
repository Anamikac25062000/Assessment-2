# 10)Write a Python function that takes a list of numbers as input and returns the sum of all the numbers divisible by 3 or 5.


input_numbers = input("Enter a list of integers separated by space: ")
list1 = list(map(int, input_numbers.split()))
new_list = []

for num in list1:
    if (num % 3 == 0 or num % 5 == 0):
        new_list.append(num)

result = sum(new_list)
print("Sum of numbers divisible by 3 or 5:", result)
