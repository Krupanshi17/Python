"""
Type Conversion & Input/Output in Python
"""

# --------------------------------------------------
# 1. IMPLICIT TYPE CONVERSION
# --------------------------------------------------
# Python automatically converts data types when it is safe

items_count = 4        # int
item_price = 99.50     # float

total_price = items_count * item_price

print("Total Price:", total_price)
print("Type of total_price:", type(total_price))


# --------------------------------------------------
# 2. EXPLICIT TYPE CONVERSION (TYPE CASTING)
# --------------------------------------------------

# String to Integer
order_id_str = "501"
order_id = int(order_id_str)

print("\nOrder ID:", order_id)
print("Type of order_id:", type(order_id))


# String to Float
rating_str = "4.7"
rating = float(rating_str)

print("Rating:", rating)
print("Type of rating:", type(rating))


# Number to String
quantity = 3
message = "Total Quantity: " + str(quantity)
print(message)


# --------------------------------------------------
# 3. BOOLEAN TYPE CONVERSION
# --------------------------------------------------

print("\nBoolean Conversions:")
print(bool(0))        # False
print(bool(1))        # True
print(bool(""))       # False
print(bool("Python")) # True


# --------------------------------------------------
# 4. COLLECTION TYPE CONVERSIONS
# --------------------------------------------------

# List to Dictionary
user_pairs = [
    ["username", "krupanshi_18"],
    ["age", 22],
    ["active", True]
]

user_data = dict(user_pairs)
print("\nUser Data Dictionary:", user_data)


# Dictionary to List
user_keys = list(user_data.keys())
user_values = list(user_data.values())

print("User Keys:", user_keys)
print("User Values:", user_values)


# Dictionary to Tuple
user_items = tuple(user_data.items())
print("User Items Tuple:", user_items)


# --------------------------------------------------
# 5. INPUT AND OUTPUT (REAL-WORLD EXAMPLE)
# --------------------------------------------------

print("\n--- User Profile Input ---")

name = input("Enter your name: ")
year_of_birth = int(input("Enter your birth year: "))

current_year = 2026
user_age = current_year - year_of_birth

print(f"\nHello {name}!")
print(f"You are {user_age} years old.")


# --------------------------------------------------
# 6. PRINT FUNCTION OPTIONS
# --------------------------------------------------

print("\nPrint Formatting Examples:")

print("Python", "Java", "C++", sep=" | ")
print("Welcome", end=" ")
print("Krupanshi")

language = "Python"
print("I love", language)
print("I love " + language)
