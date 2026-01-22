"""
POLYMORPHISM IN PYTHON

This file covers:
1. What is Polymorphism
2. Method Overriding
3. Duck Typing
4. Operator Overloading

Polymorphism means:
Same method name, different behavior.
"""

# 1. WHAT IS POLYMORPHISM?
"""
Polymorphism allows objects of different classes
to respond to the same method call in different ways.
"""

# 2. METHOD OVERRIDING (Inheritance-based Polymorphism)
"""
Method overriding occurs when a child class provides
its own implementation of a parent class method.
"""

class Payment:
    def pay(self):
        print("Processing payment")

class CreditCardPayment(Payment):
    def pay(self):
        print("Payment done using Credit Card")

class UpiPayment(Payment):
    def pay(self):
        print("Payment done using UPI")

payments = [CreditCardPayment(), UpiPayment()]

for payment in payments:
    payment.pay()

# 3. DUCK TYPING
"""
Duck Typing means Python focuses on behavior, not type.

If an object has the required method, Python allows it.
The class of the object does not matter.
"""

class Laptop:
    def start(self):
        print("Laptop is starting")

class Mobile:
    def start(self):
        print("Mobile is starting")

class Tablet:
    def start(self):
        print("Tablet is starting")

def boot_device(device):
    """
    This function does not check object type.
    It only assumes the object has a start() method.
    """
    device.start()

boot_device(Laptop())
boot_device(Mobile())
boot_device(Tablet())


# 4. WHY DUCK TYPING IS USEFUL
"""
Duck typing makes code flexible.
New classes can be added without changing existing code,
as long as they provide the expected behavior.
"""


# 5. OPERATOR OVERLOADING
"""
Operator Overloading allows operators like +, ==, *
to have custom meaning for user-defined objects.

This is done using magic methods.
"""

class ShoppingCart:
    def __init__(self, item_count):
        self.item_count = item_count

    def __add__(self, other):
        """
        Overloads the + operator.
        Combines item counts from two carts.
        """
        return self.item_count + other.item_count

cart1 = ShoppingCart(3)
cart2 = ShoppingCart(5)

print("Total items:", cart1 + cart2)


# 6. HOW OPERATOR OVERLOADING WORKS INTERNALLY
"""
cart1 + cart2 internally becomes:
cart1.__add__(cart2)
"""

print("Total items:", cart1.__add__(cart2))


# 7. OPERATOR OVERLOADING USING __eq__
"""
__eq__ is used to overload the == operator.
"""

class Box:
    def __init__(self, weight):
        self.weight = weight

    def __eq__(self, other):
        return self.weight == other.weight

box1 = Box(10)
box2 = Box(10)

print("Boxes are equal:", box1 == box2)
