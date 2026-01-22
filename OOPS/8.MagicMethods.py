"""
SPECIAL / MAGIC METHODS IN PYTHON

Magic methods allow custom behavior
for user-defined objects.

"""

# 1. __init__

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages


# 2. __str__ (User-friendly)

    def __str__(self):
        return f"Book: {self.title}, Pages: {self.pages}"


# 3. __repr__ (Developer-friendly)

    def __repr__(self):
        return f"Book('{self.title}', {self.pages})"


# 4. __len__

    def __len__(self):
        return self.pages


# 5. __add__ (Operator Overloading)

    def __add__(self, other):
        return self.pages + other.pages


# USING THE CLASS

b1 = Book("Python Basics", 300)
b2 = Book("Advanced Python", 450)

print(b1)                 # __str__
print(repr(b1))           # __repr__
print("Total pages:", len(b1))   # __len__
print("Combined pages:", b1 + b2)  # __add__
