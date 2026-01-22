"""Error Handling in Python
Error handling is a crucial aspect of programming that allows developers to manage and respond to runtime errors gracefully. 
In Python, error handling is primarily done using the try, except, else, and finally blocks. This snippet demonstrates how to 
implement error handling in Python.
Try block is used to wrap code that may potentially raise an exception. If an exception occurs, the control is transferred to 
the except block, where you can handle the error appropriately. The else block is executed if no exceptions are raised, and the 
finally block is executed regardless of whether an exception occurred or not, making it ideal for cleanup actions.
Exceptions can be specific (like ValueError, TypeError) or general (using Exception). It's a good practice to catch specific 
exceptions to avoid masking other unexpected errors.
Exception objects can provide additional information about the error, which can be useful for debugging.
"""

#Syntax Example
"""try:
    # code that may cause error
except SomeSpecificError:
    # runs if that specific error occurs
except AnotherSpecificError:
    # runs if another specific error occurs
except Exception as e:
    # runs for any other exception
    print("An error occurred:", e)
else:
    # runs if no error occurs
finally:
    # runs no matter what
    """

# Example of error handling
try:
    number=int(input("Enter a number:"))
    result=100/number
    print("Result is:",result)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")

try:
    value=int("Abc")
except (ValueError,TypeError):
    print("Conversion Error Occured!!")

try:
    number=10/0
except ZeroDivisionError as error:
    print("ZeroDivisionError occurred:", error)

def read_file(filename):
    try:
        with open(filename,"r") as f:
            return f.read()
    except FileNotFoundError:
        return "File not found.Please check the filename."
    except PermissionError:
        return "Please Check the file Permissions."
content=read_file("data.txt")
print(content)

#Example with else
try:
    number=int(input("Enter a number:"))
    result=100/number
    print("Result is:",result)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")
else:
    print("Operation completed successfully.")

#Example with finally
try:
    file=open("sample.txt","r")
    data=file.read()
    print(data)
except FileNotFoundError:
    print("File not found.")
finally:
    print("Execution completed.")


"""Custom Exception Example
Custom exceptions allow developers to create their own exception classes that can provide more specific error handling for their
applications. This snippet demonstrates how to define and use custom exceptions in Python.
To create a custom exception, you typically define a new class that inherits from the built-in Exception class. You can add additional attributes or methods to your custom exception class to provide more context about the error.
Raising a custom exception is done using the raise statement, similar to built-in exceptions.
Custom exceptions can be caught using the same try-except mechanism as built-in exceptions."""

class NegativeValueError(Exception):
    pass

def chceck_positive(number):
    if number<0:
        raise NegativeValueError("Negative Value Provided:")
    return True

try:
    chceck_positive(-5)
except NegativeValueError as e:
    print("Custom Exception Caught:",e)
    