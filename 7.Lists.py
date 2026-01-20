"""
LISTS IN PYTHON
This file explains list basics and commonly used list operations
with simple explanations and real-world oriented examples.

Topics Covered:
1. Creating Lists
2. Accessing Elements (Indexing & Slicing)
3. Updating Lists
4. Adding & Removing Elements
5. Useful List Operations
6. Real-World Examples

"""

# 1. CREATING LISTS
"""
Lists can store multiple values of different data types.
"""

employee_ids = [101, 102, 103, 104]
profile = ["Krupanshi", 22, "Intern", True]

print(employee_ids)
print(profile)


# 2. ACCESSING ELEMENTS (INDEXING & SLICING)
"""
Indexing starts at 0
Negative indexing starts from the end
"""

cities = ["Ahmedabad", "Mumbai", "Delhi", "Pune", "Jaipur"]

print(cities[1])       # Mumbai
print(cities[-2])      # Pune
print(cities[1:4])     # ['Mumbai', 'Delhi', 'Pune']
print(cities[:3])      # ['Ahmedabad', 'Mumbai', 'Delhi']
print(cities[3:])      # ['Pune', 'Jaipur']


# 3. UPDATING LIST ELEMENTS (MUTABILITY)
"""
Lists are mutable – values can be modified.
"""

ratings = [3, 4, 5]
ratings[0] = 4
print(ratings)


# 4. ADDING & REMOVING ELEMENTS
"""
append(), insert(), remove(), pop()
"""

daily_tasks = ["Login", "Check Emails"]

daily_tasks.append("Attend Meeting")
daily_tasks.insert(1, "Update Report")
print(daily_tasks)

daily_tasks.remove("Login")
removed_task = daily_tasks.pop()
print("Removed:", removed_task)
print("Remaining Tasks:", daily_tasks)


# 5. USEFUL LIST OPERATIONS

# Length of list
print("Total Tasks:", len(daily_tasks))

# Combining lists
frontend = ["HTML", "CSS"]
backend = ["Python", "Django"]
tech_stack = frontend + backend
print(tech_stack)

# Repeating list
priority = ["High"]
print(priority * 3)


# 6. LIST COMPREHENSIONS
"""
Compact way to create lists
"""

attendance = [1, 0, 1, 1, 0]
present_students = [status for status in attendance if status == 1]
print(present_students)

square_values = [num * num for num in range(1, 6)]
print(square_values)


# 7. COMMON LIST METHODS

prices = [250, 120, 300, 120]

prices.extend([400, 150])
print(prices)

print("First 120 at index:", prices.index(120))
print("120 appears:", prices.count(120), "times")

prices.sort()
print("Sorted Prices:", prices)

prices.sort(reverse=True)
print("Descending Order:", prices)


# 8. COPYING LISTS
"""
Difference between copy and reference
"""

original = ["Pen", "Notebook", "Marker"]
copy_list = original.copy()
reference_list = original

original.append("Eraser")

print("Original:", original)
print("Copy:", copy_list)
print("Reference:", reference_list)


# 9. NESTED LISTS
"""
Lists inside lists
"""

monthly_sales = [
    ["Jan", 2000],
    ["Feb", 2500],
    ["Mar", 3000]
]

print(monthly_sales[2][1])  # Sales of March


# 10. REAL-WORLD EXAMPLE: STUDENT MARKS REPORT
"""
Generating a simple student marks summary
"""

students = ["Asha", "Ravi", "Neha"]
marks = [78, 85, 90]

report = list(zip(students, marks))
print("Student Report:", report)
