"""
SETS IN PYTHON
This file explains sets and basic set operations
using simple and easy-to-understand examples.

Topics Covered:
1. Set Creation
2. Set Characteristics
3. Adding & Removing Elements
4. Set Operations
5. Set Methods
6. Simple Real-World Examples

"""


# 1. SET CREATION
"""
Sets store only unique values.
Duplicate values are removed automatically.
"""
numbers = {1, 2, 3, 2, 4, 1}
print(numbers)

empty_set = set()
print(empty_set)


# 2. SET CHARACTERISTICS
"""
- Sets are unordered
- No duplicate values
- Elements cannot be accessed by index
"""

colors = {"Red", "Blue", "Green", "Red"}
print(colors)


# 3. ADDING & REMOVING ELEMENTS
"""
Common operations on sets
"""

subjects = {"Math", "Science"}

subjects.add("English")
print(subjects)

subjects.update(["History", "Geography"])
print(subjects)

subjects.remove("Math")
print(subjects)

subjects.discard("Biology")  # no error if not found
print(subjects)

removed_item = subjects.pop()
print("Removed:", removed_item)
print("Remaining:", subjects)


# 4. SET OPERATIONS
"""
Basic set operations
"""

group_a = {10, 20, 30}
group_b = {30, 40, 50}

print(group_a | group_b)   # union
print(group_a & group_b)   # intersection
print(group_a - group_b)   # difference
print(group_a ^ group_b)   # symmetric difference


# 5. SET METHODS
"""
Some commonly used set methods
"""

items = {"Pen", "Book", "Scale"}

copy_items = items.copy()
items.clear()

print("Original after clear:", items)
print("Copied set:", copy_items)


# 6. REAL-WORLD EXAMPLE: UNIQUE STUDENT ROLLS
"""
Using set to remove duplicate roll numbers
"""

roll_numbers = [101, 102, 103, 101, 104, 102]
unique_rolls = set(roll_numbers)

print("Unique Roll Numbers:", unique_rolls)
