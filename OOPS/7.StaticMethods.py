"""
STATIC METHODS IN PYTHON

Static methods are utility functions
defined inside a class.

"""

# 1. BASIC STATIC METHOD

class Calculator:
    @staticmethod
    def multiply(a, b):
        return a * b

print("Result:", Calculator.multiply(4, 5))


# 2. STATIC METHOD FOR VALIDATION

class UserValidator:
    @staticmethod
    def validate_username(username):
        return bool(username and username.strip())

print(UserValidator.validate_username("krupanshi"))
print(UserValidator.validate_username(""))


# 3. STATIC METHOD VS CLASS METHOD

class AppConfig:
    app_name = "MyApp"

    @classmethod
    def show_app(cls):
        print("App:", cls.app_name)

    @staticmethod
    def app_version():
        return "1.0.0"

AppConfig.show_app()
print("Version:", AppConfig.app_version())


# 4. REAL-WORLD EXAMPLE
"""
Static methods are commonly used for
formatting, validation, and calculations.
"""

class EmailUtils:
    @staticmethod
    def extract_username(email):
        return email.split("@")[0]

email = "xyz@gmail.com"
print("Username:", EmailUtils.extract_username(email))
