"""If-Else Control Flow in Python
Control flow statements allow you to dictate the order in which code is executed based on certain conditions.
"""
# ==================================================
# 1. BASIC IF STATEMENT
# ==================================================
"""
The 'if' statement runs code only when a condition is True.
"""

temperature = 32

if temperature > 30:
    print("Weather is hot")


# ==================================================
# 2. IF – ELSE STATEMENT
# ==================================================
"""
The 'else' block runs when the 'if' condition is False.
"""

is_logged_in = False

if is_logged_in:
    print("Welcome back!")
else:
    print("Please login to continue")


# ==================================================
# 3. IF – ELIF – ELSE STATEMENT
# ==================================================
"""
Used when multiple conditions are checked in sequence.
"""

marks = 78

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "D"

print("Grade:", grade)

#Nested If Example
num = 15
if num > 0:
    if num % 2 == 0:
        print(f"{num} is a positive even number.")
    else:
        print(f"{num} is a positive odd number.")
else:
    print(f"{num} is not a positive number.")

# ==================================================
# 5. NESTED IF STATEMENT
# ==================================================
"""
One 'if' inside another 'if'.
"""

user_age = 20
has_id_proof = True

if user_age >= 18:
    if has_id_proof:
        print("Entry Allowed")
    else:
        print("ID Proof Required")
else:
    print("Underage - Entry Denied")


#Real-World Example: User Authentication
username = "krupanshi"
password = "secure123"

input_username = input("Enter username: ")
input_password = input("Enter password: ")

if input_username == username and input_password == password:
    print("Login successful!")
else:
    print("Invalid username or password.") 
