"""
INHERITANCE IN PYTHON

Inheritance allows a class (child) to acquire
properties and methods of another class (parent).

This file covers:
1. What is Inheritance
2. Single Inheritance
3. Multilevel Inheritance
4. Multiple Inheritance
5. Method Overriding
6. super() keyword
7. Real-world examples

Author: Krupanshi
"""

# 1. WHAT IS INHERITANCE?
"""
Inheritance is used to reuse code.
A child class inherits data and behavior from a parent class.
"""
# 2. SINGLE INHERITANCE
"""
One child class inherits from one parent class.
"""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class Developer(Employee):
    def __init__(self, name, salary, technology):
        super().__init__(name, salary)
        self.technology = technology

    def show_tech(self):
        print("Technology:", self.technology)


dev = Developer("bob", 60000, "Python")
dev.show_details()
dev.show_tech()


# 3. MULTILEVEL INHERITANCE
"""
Child inherits from parent, which inherits from another parent.
"""

class Organization:
    def org_name(self):
        print("Tech Solutions")

class Department(Organization):
    def dept_name(self):
        print("AI Department")

class Staff(Department):
    def staff_role(self):
        print("Developer")

staff = Staff()
staff.org_name()
staff.dept_name()
staff.staff_role()


# 4. MULTIPLE INHERITANCE

"""
One child inherits from multiple parent classes.
"""

class Backend:
    def backend_skill(self):
        print("Backend Development")

class Frontend:
    def frontend_skill(self):
        print("Frontend Development")

class FullStackDeveloper(Backend, Frontend):
    def role(self):
        print("Full Stack Developer")

fs = FullStackDeveloper()
fs.backend_skill()
fs.frontend_skill()
fs.role()


# 5. METHOD OVERRIDING
"""
Child class provides its own implementation
of a method defined in parent class.
"""

class Vehicle:
    def fuel_type(self):
        print("Uses fuel")

class ElectricVehicle(Vehicle):
    def fuel_type(self):
        print("Uses electricity")

ev = ElectricVehicle()
ev.fuel_type()


# 6. super() KEYWORD
"""
super() is used to call parent class methods
and constructors.
"""

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

    def show(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)

s = Student("Bob", 101)
s.show()

# 7. REAL-WORLD EXAMPLE: PAYMENT SYSTEM

"""
A real-world example where different payment methods
inherit from a common base class.
"""

class Payment:
    def __init__(self, amount):
        self.amount = amount

    def pay(self):
        print("Processing payment")


class CreditCardPayment(Payment):
    def pay(self):
        print(f"Paid {self.amount} using Credit Card")


class UpiPayment(Payment):
    def pay(self):
        print(f"Paid {self.amount} using UPI")


class CashPayment(Payment):
    def pay(self):
        print(f"Paid {self.amount} in Cash")


# Using the classes
payment1 = CreditCardPayment(500)
payment2 = UpiPayment(1200)
payment3 = CashPayment(300)

payment1.pay()
payment2.pay()
payment3.pay()
