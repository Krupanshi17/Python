"""Operators in Python are symbols that perform operations on variables and values.
There are several types of operators:
1. Arithmetic Operators
2. Comparison Operators
3. Logical Operators
4. Identity Operators
5. Membership Operators"""



# ==================================================
# 1. ARITHMETIC OPERATORS
# ==================================================
"""
Arithmetic operators are used to perform mathematical calculations.

Operator  Description
+         Addition
-         Subtraction
*         Multiplication
/         Division
//        Floor Division
%         Remainder
**        Power
"""

item_price = 199
items_ordered = 3

total_cost = item_price * items_ordered
discount = total_cost * 0.15
final_price = total_cost - discount

print("Total Cost:", total_cost)
print("Discount:", discount)
print("Final Price:", final_price)


# ==================================================
# 2. COMPARISON OPERATORS
# ==================================================
"""
Comparison operators compare two values and return True or False.

Operator  Description
==        Equal to
!=        Not equal to
>         Greater than
<         Less than
>=        Greater than or equal to
<=        Less than or equal to
"""

minimum_age = 18
user_age = 20

print("Eligible Age:", user_age >= minimum_age)
print("Is Minor:", user_age < minimum_age)


# ==================================================
# 3. LOGICAL OPERATORS
# ==================================================
"""
Logical operators are used to combine multiple conditions.

Operator  Description
and       True if all conditions are True
or        True if at least one condition is True
not       Reverses the result
"""

is_logged_in = True
has_subscription = False

print("Access Granted:", is_logged_in and has_subscription)
print("Can View Free Content:", is_logged_in or has_subscription)
print("Login Status Reversed:", not is_logged_in)


# ==================================================
# 4. IDENTITY OPERATORS
# ==================================================
"""
Identity operators check whether two variables refer to the same object in memory.

Operator   Description
is         Same object
is not     Different objects
"""

cart_items = ["apple", "banana"]
backup_cart = cart_items
new_cart = ["apple", "banana"]

print("Same Cart:", cart_items is backup_cart)
print("Different Cart Object:", cart_items is not new_cart)


# ==================================================
# 5. MEMBERSHIP OPERATORS
# ==================================================
"""
Membership operators test whether a value exists in a collection.

Operator   Description
in         Value exists
not in     Value does not exist
"""

available_coupons = ["SAVE10", "FREESHIP", "WELCOME"]

print("Coupon Applied:", "SAVE10" in available_coupons)
print("Invalid Coupon:", "DISCOUNT50" not in available_coupons)
