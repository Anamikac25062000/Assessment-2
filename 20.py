# 20) Create a Python library with the function to input the values with expectation handling and demonstrate with the example.


def get_input_safe(prompt, data_type, error_message="Invalid input. Please try again."):
    while True:
        user_input = input(prompt)
        try:
            input_value = data_type(user_input)
            return input_value
        except ValueError:
            print(error_message)

if __name__ == "__main__":
    age = get_input_safe("Enter your age: ", int)
    print(f"You entered: {age}")

    height = get_input_safe("Enter your height (in meters): ", float)
    print(f"You entered: {height}")

    name = get_input_safe("Enter your name: ", str)
    print(f"Hello, {name}!")

    is_student = get_input_safe("Are you a student? (True/False): ", lambda x: x.lower() == 'true' or x.lower() == 'false')
    print(f"You are a student: {is_student}")
