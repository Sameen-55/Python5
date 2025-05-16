def currency_converter(amount, exchange_rate=280):
    """
    Converts a given amount in USD to the target currency (default: PKR).
    
    Parameters:
    - amount (float or int): The amount in USD to convert.
    - exchange_rate (float): The conversion rate from USD to PKR (default is 280).
    
    Returns:
    - str: A message showing the converted amount in PKR.
    """
    try:
        converted_amount = amount * exchange_rate
        return f"{amount} USD is equal to {converted_amount:.2f} PKR at an exchange rate of {exchange_rate}."
    except TypeError:
        return "Please provide a numeric value for the amount and exchange rate."

# Example usage:
print(currency_converter(100))

#question 2;
def add_numbers(a, b):
    """
    Adds two numbers and returns the result.

    Parameters:
    - a (int or float): The first number.
    - b (int or float): The second number.

    Returns:
    - int or float: The sum of the two numbers.
    """
    return a + b

# Test the function
result = add_numbers(7, 5)
print("The sum is:", result)

#question 3;
def add_numbers(a, b):
    """
    Adds two numbers and returns the result.

    Parameters:
    - a (int or float): The first number.
    - b (int or float): The second number.

    Returns:
    - int or float: The sum of the two numbers.
    """
    return a + b

# Test the function
result = add_numbers(7, 5)
print("The sum is:", result)

#question 4:
def add_numbers(a, b):
    return a + b

print(add_numbers(7, 5))

#question 5;
def display_student_info(*, name, age, grade, school):
    print(f"Student Name: {name}")
    print(f"Age: {age}")
    print(f"Grade: {grade}")
    print(f"School: {school}")

# Example usage
display_student_info(name="Ali", age=14, grade="8th", school="Green Valley High")

#question 6;
def calculate_price(price, quantity):
    return price * quantity

# Example usage
total = calculate_price(150, 3)
print("Total Price:", total)

#question 7;
def display_prices(product, **prices):
    print(f"Product: {product}")
    for store, price in prices.items():
        print(f"{store}: ${price}")

# Example usage
display_prices("Laptop", Amazon=800, eBay=750, Walmart=780)

#question 8;
def find_max(*numbers):
    return max(numbers)

# Example usage
print(find_max(10, 25, 7, 42, 3))

#question 9;
def display_info(name, age, **details):
    print(f"- Name: {name}")
    print(f"- Age: {age}")
    if details:
        print("- Other Details:")
        for key, value in details.items():
            print(f"    - {key}: {value}")

# Example usage
display_info(
    "Alice", 30,
    address="123 Main St",
    phone="123-456-7890",
    email="alice@example.com"
)
#question 10;
products = [
    {"name": "Laptop", "price": 1200, "in_stock": True, "discount": 0.1},
    {"name": "Smartphone", "price": 800, "in_stock": False, "discount": 0.05},
    {"name": "Headphones", "price": 150, "in_stock": True, "discount": 0.2},
    {"name": "Smartwatch", "price": 300, "in_stock": True, "discount": 0},
    {"name": "Keyboard", "price": 100, "in_stock": True, "discount": 0.15}
]

# Get names of in-stock products
in_stock_names = [product["name"] for product in products if product["in_stock"]]

# Calculate final prices for in-stock products after discount
discounted_prices
#question 11;
even_numbers = [num for num in range(1, 21) if num % 2 == 0]
print(even_numbers)

#question 12;
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
divisible_by_3_or_5 = [num for num in numbers if num % 3 == 0 or num % 5 == 0]
print(divisible_by_3_or_5)



