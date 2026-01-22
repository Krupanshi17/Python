"""
DECORATORS IN PYTHON

Decorators allow modification of functions
without changing their original code.

"""

# 1. BASIC DECORATOR

def simple_logger(func):
    def wrapper():
        print("Function is about to run")
        func()
        print("Function finished running")
    return wrapper


@simple_logger
def say_hello():
    print("Hello, World!")

say_hello()


# 2. DECORATOR WITH ARGUMENTS

def execution_logger(func):
    def wrapper(*args, **kwargs):
        print("Arguments:", args, kwargs)
        return func(*args, **kwargs)
    return wrapper


@execution_logger
def add(a, b):
    return a + b

print("Result:", add(10, 20))


# 3. REAL-WORLD EXAMPLE: AUTHENTICATION

def login_required(func):
    def wrapper(user):
        if user != "admin":
            print("Access denied")
            return
        return func(user)
    return wrapper


@login_required
def view_dashboard(user):
    print("Welcome to dashboard")

view_dashboard("admin")
view_dashboard("guest")
