#13) Implement a program that simulates a basic calculator, allowing users to perform arithmetic operations (addition, subtraction, multiplication, division) on two numbers.


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def calculator():
    operations = {'+': add, '-': subtract, '*': multiply, '/': divide}

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Enter the operator (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numerical values.")
            continue

        if operator in operations:
            result = operations[operator](num1, num2)
            print(f"\nResult: {result}\n")
        else:
            print("Invalid operator. Please enter a valid operator (+, -, *, /).")

calculator()