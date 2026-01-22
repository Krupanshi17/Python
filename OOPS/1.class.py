
"""
Object Oriented Programming

| Term   | Meaning            |
| --------- | --------------------- |
| Class     | Blueprint             |
| Object    | Instance of class     |
| Attribute | Data                  |
| Method    | Function inside class |

 #Benefits of OOP
Code reusability
Easy maintenance
Scalability
Cleaner design

#When should you use OOP?

Use OOP when:

    problem is complex

    multiple entities interact

    code needs to scale
"""

class Employee:
    def calculate_salary(self,rate,hours):
        return rate*hours
    
"""
CLASS & OBJECT IN PYTHON

This file explains:
1. What is a Class
2. What is an Object
3. Instance Variables
4. Methods
5. Constructor (__init__)
6. Role of self
7. Real-world example

"""

# 1. WHAT IS A CLASS?
"""
A class is a blueprint or template.
It defines what data and behavior an object will have.
"""

class Student:
    pass

# 2. WHAT IS AN OBJECT?
"""
An object is a real instance created from a class.
Each object has its own data.
"""

s1 = Student()
s2 = Student()

print(s1)
print(s2)

# 3. INSTANCE VARIABLES
"""
Instance variables store data unique to each object.
They are created using self.
"""

class Person:
    def set_details(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


p1 = Person()
p1.set_details("Alex", 22)
p1.show_details()

p2 = Person()
p2.set_details("Bob", 24)
p2.show_details()

# 4. METHODS
"""
Methods are functions defined inside a class.
They describe the behavior of an object.
"""

class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
print("Sum:", calc.add(10, 20))

# 5. CONSTRUCTOR (__init__)
"""
__init__ is a special method that runs automatically
when an object is created.
It is used to initialize data.
"""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


e1 = Employee("Pitter", 35000)
e2 = Employee("Alice", 42000)

e1.display()
e2.display()


# 6. ROLE OF self
"""
self refers to the current object.
It allows access to instance variables and methods.
"""

class Car:
    def set_brand(self, brand):
        self.brand = brand

    def show_brand(self):
        print("Car Brand:", self.brand)


c = Car()
c.set_brand("Toyota")
c.show_brand()

# 7. REAL-WORLD EXAMPLE
"""
Modeling a Bank Account using class and object.
"""

class BankAccount:
    def __init__(self, holder_name, balance):
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def show_balance(self):
        print(self.holder_name, "Balance:", self.balance)


account = BankAccount("Tyen", 5000)
account.deposit(2000)
account.show_balance()
