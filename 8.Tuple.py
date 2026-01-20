"""
TUPLES IN PYTHON
This file explains tuples, their properties, and usage
with practical and real-world examples.

Topics Covered:
1. Tuple Creation
2. Accessing Tuple Elements
3. Tuple Immutability
4. Tuple Operations
5. Tuple Methods
6. Packing & Unpacking
7. Real-World Examples

"""

# 1. TUPLE CREATION
"""
Tuples are ordered and immutable collections.
They are defined using parentheses ().
"""

user_info = ("Krupanshi", 22, "Python Intern")
single_value = (100,)   # comma is required

print(user_info)
print(single_value)


# 2. ACCESSING TUPLE ELEMENTS
"""
Accessing elements is similar to lists.
"""

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

print(days[0])        # Monday
print(days[-1])       # Friday
print(days[1:4])      # ('Tuesday', 'Wednesday', 'Thursday')



# 3. TUPLE IMMUTABILITY
"""
Tuples cannot be modified after creation.
"""

scores = (85, 90, 88)
# scores[0] = 95   # ❌ This will raise an error
print(scores)


# 4. TUPLE OPERATIONS

numbers1 = (1, 2, 3)
numbers2 = (4, 5)

combined = numbers1 + numbers2
repeated = numbers2 * 2

print(combined)
print(repeated)


# 5. TUPLE METHODS
"""
Tuples have only two built-in methods:
count() and index()
"""

data = (10, 20, 30, 20, 40)

print(data.count(20))   # number of occurrences
print(data.index(30))   # index of first occurrence


# 6. TUPLE PACKING & UNPACKING
"""
Packing: Assigning multiple values to a tuple
Unpacking: Extracting values from a tuple
"""

employee = ("EMP101", "Krupanshi", "IT")

emp_id, emp_name, department = employee

print(emp_id)
print(emp_name)
print(department)


# 7. NESTED TUPLES
"""
Tuples inside tuples
"""

office_locations = (
    ("Ahmedabad", "Gujarat"),
    ("Pune", "Maharashtra"),
    ("Jaipur", "Rajasthan")
)

print(office_locations[1][0])  # Pune


# 8. REAL-WORLD EXAMPLE 1: CONSTANT CONFIGURATION
"""
Tuples are used where values should not change.
"""

APP_CONFIG = ("localhost", 8080, "DEBUG")

print("Host:", APP_CONFIG[0])
print("Port:", APP_CONFIG[1])


# 9. REAL-WORLD EXAMPLE 2: STUDENT RECORDS
"""
Using tuples to store fixed student records.
"""

student_records = (
    ("Asha", 85),
    ("Ravi", 78),
    ("Neha", 92)
)

for student in student_records:
    name, marks = student
    print(f"{name} scored {marks}")
