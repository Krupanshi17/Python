"""List Comprehension
List comprehensions provide a concise way to create lists.
They consist of brackets containing an expression followed by a for clause, and can include optional if clauses.
List comprehensions are generally more compact and faster than traditional for loops for creating lists.
"""

"""Basic Syntax:
[expression for item in iterable]"""

#example 
numbers=[i*2 for i in range(1,11)]
print(numbers)

l1=["apple","banana","cherry","date"]
l2=[i[:-2]+i[-2].upper()+i[-1] for i in l1]
print(l2)

pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
print(pairs)


prices=[100,150.200,250,300]
expensive_prices=[p for p in prices if p>250]
print(expensive_prices)

names=['alice','bob','charlie','david']
final_names=[name.capitalize() for name in names ]
print(final_names)


"""Dictionary Comprehension
Dictionary comprehensions provide a concise way to create dictionaries.
They consist of curly braces containing key-value pairs followed by a for 
clause, and can include optional
if clauses."""

"""Basic Syntax:
{key_expression: value_expression for item in iterable}"""

squares={x:x*x for x in range(1,6)}
print(squares)

score={'A':85,'B':90,'C':43}

passed={k:v for k,v in score.items() if v>=50}
print(passed)

prices={'A':100,'B':200,'C':300}

updated_prices={k:v+20 for k,v in prices.items() if v>=300}
print(updated_prices)

"""Generator Comprehension
Generator comprehensions provide a concise way to create generators.
They are similar to list comprehensions but use parentheses instead of square brackets.
Generator comprehensions are more memory efficient than list comprehensions because 
they generate items on-the-fly"""

# Example of a generator comprehension
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