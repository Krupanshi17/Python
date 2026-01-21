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

"""Default arguments allow you to specify default values for parameters in case no argument is provided during the function call.
This makes the function more flexible and easier to use."""

#Example of Default Arguments
def greet(name,city="Ahmedabad"):
    print(name,"lives in",city)
greet("Alex")
greet("Alex","Surat")

"""Keyword arguments mean you pass values using parameter names, not position.
So Python knows which value goes where, regardless of order."""

#Example of Keyword Arguments
def person(name,age):
    print("Name:",name,"Is",age,"years old")
person(age=30,name="Jhon")
person(name="bob",age=30)


"""*args allows a function to accept any number of positional arguments
Inside the function, args becomes a tuple"""
#Example of *args

def calculate_average(*marks):
    total=sum(marks)
    average=total/len(marks)
    return average
print("Average Marks:",calculate_average(80,90,85))
print("Average Marks:",calculate_average(70,75,80,85,90,44,60))


"""**kwargs allows a function to accept any number of keyword arguments
Inside the function, kwargs becomes a dictionary"""

#Example of **kwargs
def personal_info(**info):
    for key,value in info.items():
        print(key+":",value)
personal_info(name="Alice",age=25,city="New York")
personal_info(name="Bob",profession="Engineer")


"""Lambda Functions
Lambda functions are small anonymous functions defined using the lambda keyword.
They can take any number of arguments but can only have one expression.
They are often used for short, throwaway functions."""
"""lambda arguments : expression"""

#Examples of Lambda Functions
square=lambda x:x*x
print(square(5))

calculated_price=lambda price,discount:price-(price*discount/100)
print(calculated_price(1000,10))

add=lambda a,b:a+b
print(add(10,20))

"""map(), filter(), and reduce() with Lambda Functions
These are functional programming tools used to work with collections (lists, tuples, etc.) in a clean way.These functions are used for functional programming in Python.
map() applies a function to all items in an iterable.
filter() filters items in an iterable based on a condition.
reduce() reduces an iterable to a single value using a binary function. 
"""

#Example of map() with Lambda
numbers=[1,2,3,4,5]
squared_numbers=list(map(lambda x:x**2,numbers))
print(squared_numbers)

#example of filter() with Lambda
numbers=[10,15,20,25,30,35]
odd_numbers=list(filter(lambda x:x%2!=0,numbers))
print(odd_numbers)

#Example of reduce() with Lambda
from functools import reduce
numbers=[1,2,3,4,5]
add=reduce(lambda x,y:x+y,numbers)
print(add)

