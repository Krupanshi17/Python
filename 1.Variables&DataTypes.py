"""Variable is a container for storing data values.
In Python, you don't need to declare the type of variable explicitly."""


# Variable names can include letters, numbers, and underscores
# but cannot start with a number or contain special characters.

valid_username_1 = "krupanshi"
valid_username_2 = "krupanshi_18"
valid_username_3 = "user_123"
valid_username_4 = "admin_user"

print(valid_username_1)
print(valid_username_2)
print(valid_username_3)
print(valid_username_4)

"""nvalid because it starts with a number
invalid_username_1 = "1krupanshi"

invalid because it contains a hyphen
invalid_username_2 = "krupanshi-user"

invalid because it contains space
invalid_username_3 = "krupanshi user"

Invalid because it uses special character
invalid_username_4 = "krupanshi@123"""

# Data Types in Python  
# Common data types include:  
# 1. Integer (int): Whole numbers
# 2. Float (float): Decimal numbers
# 3. String (str): Text
# 4. Boolean (bool): True or False  

"""
TOPIC 3: DATA TYPES
Real-world example: User Profile
"""

user_id = 102            # int
user_name = "krupanshi"  # str
user_age = 22            # int
account_balance = 1500.50  # float
is_premium_user = False  # bool

print("User ID:", user_id, type(user_id))
print("Username:", user_name, type(user_name))
print("Age:", user_age, type(user_age))
print("Balance:", account_balance, type(account_balance))
print("Premium User:", is_premium_user, type(is_premium_user))
