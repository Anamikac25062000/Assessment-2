#11) Write a Python function called calculate_discounted_price that takes the original price of an item and a discount percentage as input. The function should return the discounted price after applying the discount. Ensure that the function handles the case where the discount percentage is negative and raises a custom exception called Invalid DiscountError with an appropriate error message.


def calculate_discounted_price(original_price, discount_percentage):
    if discount_percentage < 0:
        print("Error: Discount percentage cannot be negative")
        return None

    discounted_price = original_price - (original_price * discount_percentage / 100)
    return discounted_price

original_price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))

result = calculate_discounted_price(original_price, discount_percentage)

if result is not None:
    print(f"Discounted price: {result}")
