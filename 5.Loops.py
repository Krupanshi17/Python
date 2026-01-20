"""
LOOPS IN PYTHON
This file covers different types of loops in Python with examples.

Types of Loops:
1. For Loop
2. While Loop
3. Nested Loops
4. Break and Continue Statements
5. Pass Statement

"""

# 1. FOR LOOP
"""
A for loop is used to iterate over a sequence (list, tuple, string, range).
"""

students = ["Amit", "Neha", "Riya", "Karan"]

print("Student List:")
for student in students:
    print(student)


# 2. WHILE LOOP
"""
A while loop runs as long as the condition is True.
"""

print("\nPassword Attempts:")
attempt = 1

while attempt <= 3:
    print(f"Attempt {attempt}")
    attempt += 1


# 3. NESTED LOOPS
"""
A loop inside another loop.
Commonly used in matrices, patterns, reports.
"""

print("\nWeekly Attendance Report:")

days = ["Mon", "Tue", "Wed"]
employees = ["Emp1", "Emp2", "Emp3"]

for day in days:
    print(f"{day}:")
    for emp in employees:
        print(f"  {emp} - Present")


# 4. BREAK STATEMENT
"""
The break statement exits the loop immediately.
"""

print("\nSearching for defective product:")

products = ["OK", "OK", "OK", "DEFECT", "OK"]

for status in products:
    if status == "DEFECT":
        print("Defective product found. Stopping check.")
        break
    print("Product checked:", status)


# 5. CONTINUE STATEMENT

"""
The continue statement skips the current iteration.
"""

print("\nProcessing Orders:")

orders = [1001, 1002, None, 1003, 1004]

for order in orders:
    if order is None:
        print("Invalid order skipped")
        continue
    print("Order processed:", order)


# 6. PASS STATEMENT
"""
The pass statement does nothing.
Used as a placeholder for future code.
"""

print("\nFeature Under Development:")

for feature in ["Login", "Payment", "Notification"]:
    if feature == "Payment":
        pass  # Will be implemented later
    else:
        print(feature, "module ready")


# 7. REAL-WORLD EXAMPLE: SHOPPING CART TOTAL
"""
Calculate total bill amount for items in a cart.
"""

cart_items = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500
}

total_amount = 0

for price in cart_items.values():
    total_amount += price

print("\nTotal Cart Amount:", total_amount)
