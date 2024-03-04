# 21) Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.


def perform_operation_on_list(my_list, index):
    try:
        result = my_list[index] ** 2 
        print(f"The result of squaring the element at index {index} is: {result}")
    except IndexError:
        print(f"Error: Index {index} is out of range for the given list.")

if __name__ == "__main__":
    sample_list = [1, 2, 3, 4, 5]

    perform_operation_on_list(sample_list, 2)
    perform_operation_on_list(sample_list, 5)  
    perform_operation_on_list(sample_list, -1)  
