#7) Write a function that takes a list of numbers as input and returns the second-largest number.


input_numbers = input("Enter elements of list separated by space: ")
input_list = list(map(int, input_numbers.split()))

def second_largest(numbers):
    if len(numbers) < 2:
        return "please enter minimum two objects"

    unique_numbers = list(set(numbers))

    if len(unique_numbers) < 2:
        return "List must have at least two unique elements"

    max_value = max(unique_numbers)
    unique_numbers.remove(max_value)

    second_largest_value = max(unique_numbers)

    return second_largest_value


result = second_largest(input_list)
print("Second-largest number:", result)
