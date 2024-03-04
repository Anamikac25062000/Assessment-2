# 22) Write a Python program input and add two integers only and handle the exceptions
# RUN 1:
# Enter First Value: 10
# Enter Second Value: 20
# 0.5
# RUN 2:
# Enter First Value: 10
# Enter Second Value: Hello
# Pls Input Integer Only invalid literal for int() with base 10: 'Hello'
# RUN 3:
# Enter First Value: 10
# Enter Second Value: 0
# Second Number Should Not Be Zero division by zero


def add_two_integers():
    try:
        first_value = int(input("Enter First Value: "))
        second_value = int(input("Enter Second Value: "))

        if second_value == 0:
            raise ValueError("Second Number Should Not Be Zero")

        result = first_value / second_value
        print(f"The result of the division is: {result}")

    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except ZeroDivisionError:
        print("Second Number Should Not Be Zero")

if __name__ == "__main__":

    add_two_integers()
