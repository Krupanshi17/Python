"""
ENCAPSULATION IN PYTHON

Encapsulation is the concept of binding data (variables)
and methods together and restricting direct access
to sensitive data.
"""
# 1. WHAT IS ENCAPSULATION?
"""
Encapsulation protects internal data of an object.
Data should not be modified directly from outside.
"""
# 2. PUBLIC MEMBER EXAMPLE
"""
Public variables are accessible everywhere.
There is no restriction.
"""

class User:
    def __init__(self, username):
        self.username = username   # public variable

    def show_user(self):
        print("User:", self.username)


u = User("Bob")
u.show_user()
print(u.username)  # allowed (public)


# 3. PROTECTED MEMBER EXAMPLE (_variable)
"""
Protected members should not be accessed directly.
This is a convention, not strict protection.
"""

class Account:
    def __init__(self, balance):
        self._balance = balance  # protected variable

    def show_balance(self):
        print("Balance:", self._balance)


acc = Account(5000)
acc.show_balance()
print(acc._balance)  # allowed but discouraged


# 4. PRIVATE MEMBER EXAMPLE (__variable)
"""
Private members cannot be accessed directly.
Python applies name mangling internally.
"""

class SecureAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def show_balance(self):
        print("Balance:", self.__balance)


secure = SecureAccount(8000)
secure.show_balance()

# print(secure.__balance)  # Not allowed

# 5. GETTER & SETTER (CONTROLLED ACCESS)
"""
Getters and setters provide safe access to private data.
"""

class Wallet:
    def __init__(self, amount):
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def set_amount(self, value):
        if value >= 0:
            self.__amount = value
        else:
            print("Invalid amount")


w = Wallet(2000)
print(w.get_amount())
w.set_amount(3000)
print(w.get_amount())

# 6. REAL-WORLD EXAMPLE: BANK ACCOUNT
"""
A bank account hides balance and allows
only deposit and withdrawal.
"""

class BankAccount:
    def __init__(self, holder_name, balance):
        self.holder_name = holder_name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


account = BankAccount("Bob", 5000)
account.deposit(2000)
account.withdraw(1500)
print("Current Balance:", account.get_balance())

