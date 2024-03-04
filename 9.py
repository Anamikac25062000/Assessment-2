# 9) Write a Python function that takes a list of integers as input and returns a new list with only the numbers that are perfect squares.


input_numbers = input("Enter a list of integers separated by space: ")
list1 = list(map(int, input_numbers.split()))
list_of_perfect_numbers = []

def is_perfect(num):
    sum_of_divisors = sum([i for i in range(1, num) if num % i == 0])
    return sum_of_divisors == num

for num in list1:
    if is_perfect(num):
        list_of_perfect_numbers.append(num)

print("List of perfect numbers:", list_of_perfect_numbers)
