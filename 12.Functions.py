""""Functions in Python
A function is a block of reusable code that performs a specific task.
Functions help in organizing code, improving readability, and avoiding repetition.
Functions are defined using the 'def' keyword followed by the function name and parentheses.
They can take parameters (inputs) and can return values (outputs).
This file explains commonly used built-in functions
with simple explanations and real-world examples."""

# 1. BASIC FUNCTION

def greet():
    print("Hello, welcome to Python learning")

greet()

# 2. FUNCTION WITH PARAMETER

def greet_user(name):
    print("Hello", name)

greet_user("Krupanshi")

def calculateGmean(a,b):
    mean=(a*b)/(a+b)
    print("Geometric Mean is:",mean)

calculateGmean(4,5)
calculateGmean(10,20)

# 3. FUNCTION WITH RETURN VALUE
def add_numbers(a, b):
    return a + b

print("Sum:", add_numbers(10,5))

# 4. FUNCTION WITH MULTIPLE CALLS

def square(num):
    return num * num

print(square(3))
print(square(6))

# 5. REAL-WORLD EXAMPLE: TOTAL MARKS
student_marks = [78, 85, 90]
def calculate_total_marks(marks):
    total = 0
    for m in marks:
        total += m
    return total

print("Total Marks:", calculate_total_marks(student_marks))

"""Parameters are the variables written inside the function definition.
They act as inputs.
Arguments are the actual values passed to the function when it is called.
They are the real data you provide to the function."""

def greet(name):
    print("Hello", name)#name is parameter
greet("Krupanshi")#Krupanshi is argument

# Function with parameters and return value

def calculate_total_price(price, quantity):
    total = price * quantity
    return total

final_amount = calculate_total_price(250, 3)
print("Total Amount:", final_amount)

