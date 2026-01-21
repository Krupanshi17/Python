"""Generator Functions in Python
Generators are a special type of function that return an iterator.
They allow you to iterate through a sequence of values without storing them all in memory at once.
This is especially useful for large datasets or infinite sequences.
Generators are defined using the yield statement instead of return.
When a generator function is called, it does not execute the function body immediately.
Instead, it returns a generator object.
The function body is executed only when the next() function is called on the generator object.
Each time next() is called, the function runs until it hits a yield statement, which produces a value and pauses the function's state.
When next() is called again, the function resumes execution right after the yield statement.
This continues until the function runs to completion, at which point a StopIteration exception is raised."""


# Example of a simple generator function

def get_numbmbers():
    yield 1
    yield 2
    yield 3
    
# Create a generator object
gen=get_numbmbers()

print(next(gen))
print(next(gen))
print(next(gen))

# Example of using a generator in a loop
def count_up_to(n):
    count=1
    while count <= n:
        yield count
        count +=1

counter=count_up_to(5)

for number in counter:
    print(number)


"""Generator to produce Fibonacci sequence"""
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for i in range(10):
    print(next(fib))

"""Generator Expressions
Generator expressions are a concise way to create generators.
They are similar to list comprehensions but use parentheses instead of square brackets.
Generator expressions are more memory efficient than list comprehensions because they generate items on-the-fly and do not store the entire list in memory.
"""

# Example of a generator expression
squared=(x*x for x in range(1,6))
for num in squared:
    print(num)

odd_numbers=(x for x in range(1,10) if x%2!=0)
for odd in odd_numbers:
    print(odd)


large_numbers = (n for n in range(1, 1000000) if n % 2 == 0)
for num in large_numbers:
    print(num)
    break  # Print only the first even number to demonstrate memory efficiency


