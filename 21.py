# 21) Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.


def division_of_list(list1, index):
    try:
        result = list1[index] / 2
        print(f"The result of dividing the element at index {index} is: {result}")
    except IndexError:
        if index < 0:
            print(f"Error: Negative index {index} is out of range for the given list.")
        else:
            print(f"Error: Index {index} is out of range for the given list.")

if __name__ == "__main__":
    input_numbers = input("Enter a list of integers separated by space: ")
    list1 = list(map(int, input_numbers.split()))

    division_of_list(list1, 2)
    division_of_list(list1, 5)
    division_of_list(list1, -1)
