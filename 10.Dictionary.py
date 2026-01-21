"""
DICTIONARIES IN PYTHON
This file explains dictionaries and common dictionary operations
using simple and different examples.

Topics Covered:
1. Dictionary Creation
2. Accessing Data
3. Modifying Data
4. Removing Data
5. Looping Through Dictionary
6. Dictionary Comprehensions
7. Nested Dictionaries
8. Useful Dictionary Methods
9. Sorting Dictionary Data

"""

# 1. DICTIONARY CREATION

product = {"id": 101, "name": "Mouse", "price": 799}
print(product)

print(product.items())
print(product.keys())
print(product.values())

# 2. ACCESSING DATA
print("product name:",product["name"])
print(product.get("price"))
print(product.get("id"))
print(product.get("brand", "No brand specified"))

# 3. MODIFYING DATA
product["price"]=899
product["id"]=102
print(product)

# 4. REMOVING DATA
product.pop("id")
print(product)

product.popitem() #removes last inserted item
print(product)

del product["name"]
print(product)

# 5. LOOPING THROUGH DICTIONARY

sales={"January":1500,"February":1800,"March":1200}

for mon in sales:
    print(mon,sales[mon])

# 6. DICTIONARY COMPREHENSIONS
numbers={n:n+10 for n in range(5)}
print(numbers)

number_even={n:n*2 for n in range(10) if n%2==0}
print(number_even)

number_odd={n:n**2 for n in range(10) if n%2!=0}
print(number_odd)

# 7. NESTED DICTIONARIES
orders={
    1:{"product":"Laptop","price":50000},
    2:{"product":"Mouse","price":800},
    3:{"product":"Keyboard","price":1500}
}

print(orders)
print(orders[2]["price"])

# 8. USEFUL DICTIONARY METHODS
fields={"name","emai","phone"}
user_data=dict.fromkeys(fields,"Not Provided")
print(user_data)


# setdefault()
account = {"name": "Krupanshi"}
print(account.setdefault("status", "Active"))
print(account)

# 9. SORTING DICTIONARY DATA
ratings = {"p": 4, "q": 2, "r": 5}

print(sorted(ratings))
print(sorted(ratings.items()))
print(sorted(ratings.items(), key=lambda x: x[1]))