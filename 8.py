# 8) Write a Python program that takes a list of integers as input and returns a new list with only the numbers that are prime.


input_numbers = input("Enter a list of integers separated by space: ")
list1 = list(map(int, input_numbers.split()))
list_of_prime_numbers = []

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for num in list1:
    if is_prime(num):
        list_of_prime_numbers.append(num)

print("List of prime numbers:", list_of_prime_numbers)

