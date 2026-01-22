"""
DATACLASSES IN PYTHON
Dataclasses simplify class creation
by automatically generating methods.
"""

from dataclasses import dataclass

# 1. BASIC DATACLASS

@dataclass
class Student:
    name: str
    age: int

s1 = Student("Bob", 22)
s2 = Student("Alex", 22)

print(s1)
print("Objects equal:", s1 == s2)


# 2. DATACLASS WITH DEFAULT VALUE

@dataclass
class Employee:
    name: str
    role: str = "Developer"

e = Employee("Bob")
print(e)


# 3. IMMUTABLE DATACLASS

@dataclass(frozen=True)
class Coordinates:
    x: int
    y: int

point = Coordinates(10, 20)
print(point)

# point.x = 30  # Not allowed


# 4. REAL-WORLD EXAMPLE
"""
Representing a product in an e-commerce system.
"""

@dataclass
class Product:
    id: int
    name: str
    price: float

p = Product(101, "Laptop", 55000.0)
print(p)
