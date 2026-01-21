"""
BUILT-IN FUNCTIONS IN PYTHON
This file explains commonly used built-in functions
with simple explanations and real-world examples.

"""
# 1. len() – Find number of items
students=["Alice","Bob","Charlie"]
print("Number of Students:",len(students))

message="Hello World"
print("Lemgth of Message",len(message))

# 2. type() – Check data type
age=25
name="John"
score=[80,90,65]

print(type(age))
print(type(name))
print(type(score))

# 3. sum(), min(), max()
marks=[85,90,78,92,88]

print("Total Marks:",sum(marks))
print("Minimun Marks:",min(marks))
print("Maximum Marks:",max(marks))

# 4. sorted() – Sort data

marks=[85,90,78,92,88]

print("Marks:",marks)
print("Sorted Marks (using sorted()):",sorted(marks))
print("Sorted Marks (Descending):",sorted(marks,reverse=True))

## 5. abs() and round()

number=-3.7
print("Absolute Value:",abs(number))
number1=7.88
print("Rounded Value:",round(number1))

# 6. any() and all()
attendence=[True,True,False,True]
print("Any Present:",any(attendence))
print("All Present:",all(attendence))

# 7. enumerate() – Get index and value
fruits=["Apple","Banana","Cherry"]
for index,fruit in enumerate(fruits):
    print( index,":",fruit)   

# 8. zip() – Combine iterables
names=["Alice","Bob","Charlie"]
ages=[25,30,22]

combined=list(zip(names,ages))
print("Combined List:",combined)

for n,a in zip(names,ages):
    print(n ,"is",a,"Years Old")
    