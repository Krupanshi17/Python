"""
@property DECORATOR IN PYTHON

@property allows controlled access to attributes
using getter and setter methods.

"""

# 1. BASIC PROPERTY WITH GETTER & SETTER

class Account:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        """
        Getter: returns account balance
        """
        return self._balance

    @balance.setter
    def balance(self, amount):
        """
        Setter: validates balance before updating
        """
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = amount


acc = Account(5000)
print("Balance:", acc.balance)

acc.balance = 7000
print("Updated Balance:", acc.balance)


# 2. READ-ONLY PROPERTY

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width


rect = Rectangle(10, 5)
print("Area:", rect.area)


# 3. REAL-WORLD EXAMPLE
"""
Protecting user age using @property
"""

class User:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 18:
            raise ValueError("User must be at least 18 years old")
        self._age = value


user = User(22)
print("Age:", user.age)

user.age = 25
print("Updated Age:", user.age)
