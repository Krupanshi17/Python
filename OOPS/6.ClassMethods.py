"""
CLASS METHODS IN PYTHON

Class methods operate on class-level data
and use the cls parameter instead of self.

"""

# 1. BASIC CLASS METHOD

class College:
    college_name = "ABC College"

    @classmethod
    def show_college(cls):
        print("College:", cls.college_name)

College.show_college()


# 2. CLASS METHOD VS INSTANCE METHOD

class Employee:
    company = "Tech Corp"

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)

    @classmethod
    def show_company(cls):
        print("Company:", cls.company)


e = Employee("Alex")
e.show_name()
Employee.show_company()


# 3. CLASS METHOD AS ALTERNATIVE CONSTRUCTOR

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @classmethod
    def from_text(cls, text):
        """
        Creates Student object from a string.
        """
        name, marks = text.split(":")
        return cls(name, int(marks))


s1 = Student.from_text("Bob:85")
print(s1.name, s1.marks)


# 4. REAL-WORLD EXAMPLE
"""
All users belong to the same application,
but can be created from different data sources.
"""

class AppUser:
    app_name = "Learning App"

    def __init__(self, username):
        self.username = username

    @classmethod
    def from_email(cls, email):
        username = email.split("@")[0]
        return cls(username)

    def show_user(self):
        print(self.username, AppUser.app_name)


user = AppUser.from_email("xyz@gmail.com")
user.show_user()
