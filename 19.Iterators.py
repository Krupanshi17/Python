"""
ITERATORS IN PYTHON

An iterator is an object that allows us to access elements
one at a time and remembers its current position.

"""

# 1. Iterable vs Iterator
# Iterable: object you can loop over (list, tuple, string)
# Iterator: object that returns values one by one using next()

numbers = [10, 20, 30]      # iterable
iterator_obj = iter(numbers)   # converting iterable to iterator

print(next(iterator_obj))  # 10
print(next(iterator_obj))  # 20
print(next(iterator_obj))  # 30

# next(iterator_obj)  # StopIteration error (no values left)


# 2. How for-loop works internally
names = ["Asha", "Ravi", "Neha"]

it = iter(names)
while True:
    try:
        print(next(it))
    except StopIteration:
        break

# 3. Iterator remembers its state
values = [1, 2, 3]
it2 = iter(values)

print(next(it2))  # 1
print(next(it2))  # 2
# it2 remembers where it stopped


# 4. Generator is also an iterator
gen = (x * x for x in range(3))

print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 4


# 5. Real-world example: Reading data step-by-step
data_stream = ["packet1", "packet2", "packet3"]
stream_iterator = iter(data_stream)

print(next(stream_iterator))  # packet1
print(next(stream_iterator))  # packet2
print(next(stream_iterator))  # packet3


#__next()__ and __iter()__

"""
Custom iterator using __iter__() and __next__().

Author: Krupanshi
"""

class CountUp:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration


# Using the custom iterator
counter = CountUp(5)

for number in counter:
    print(number)
