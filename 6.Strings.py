"""
STRINGS IN PYTHON
This file covers string operations and methods with real-world examples.
It is immutable, meaning once created, it cannot be changed.
Topics Covered:
1. String Creation
2. String Indexing & Slicing
3. Common String Methods
4. String Formatting
5. Real-World Example

"""

# 1. STRING CREATION
"""
Strings are sequences of characters enclosed in quotes.
"""

user_name = "Krupanshi"
email = "krupanshi@gmail.com"

print(user_name)
print(email)


# 2. STRING INDEXING & SLICING
"""
Indexing starts from 0.
Negative indexing starts from -1.
"""

course = "PythonProgramming"

print(course[0])     
print(course[-1])     
print(course[0:6])   
print(course[6:])     


# 3. COMMON STRING METHODS
"""
String methods return new strings.
Original string remains unchanged.
"""

message = "  welcome to Python Internship  "

print(message.upper())
print(message.lower())
print(message.strip())
print(message.replace("Internship", "Training"))
print(message.count("o"))
print(message)

name=["Krupanshi","Gandhi"]
full_name=" ".join(name)
print(full_name)

# 4. STRING FORMATTING
"""
Formatting is used to insert variables into strings.
"""

age = 22
city = "Ahmedabad"

# f-string (recommended)
print(f"My age is {age} and I live in {city}")

# format() method
print("My age is {} and I live in {}".format(age, city))


# 5. REAL-WORLD EXAMPLE: EMAIL VALIDATION (BASIC)
"""
Check if email contains basic required characters.
"""

user_email = "krupanshi@gmail.com"

if "@" in user_email and "." in user_email:
    print("Valid email format")
else:
    print("Invalid email format")
