"""Nested Functions and Closures in Python
Nested functions are functions defined within other functions. They can be useful for encapsulating functionality and creating closures.
A closure is a nested function that captures variables from its enclosing scope. This allows the nested function to remember the values of those variables even after the outer function has finished executing.
Closures are often used for data hiding and creating function factories."""

def outer(number):
    def inner():
        return number + 10
    return inner

closure_function = outer(5)
print(closure_function())  # Output: 15


def power(exponent):
    def calculate(base):
        return base ** exponent
    return calculate

square = power(2)
cube = power(3)

print(square(4))
print(cube(4))
