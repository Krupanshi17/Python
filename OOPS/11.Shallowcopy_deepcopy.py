"""
SHALLOW COPY VS DEEP COPY IN PYTHON

This file explains how object copying works
and why shallow and deep copy behave differently.

"""

import copy

# 1. SHALLOW COPY
"""
Shallow copy duplicates the outer object,
but nested objects are shared.
"""

original_list = [[1, 2], [3, 4]]

shallow_copy = copy.copy(original_list)

print("Before modification:")
print("Original:", original_list)
print("Shallow :", shallow_copy)

shallow_copy[0][0] = 99

print("\nAfter modifying shallow copy:")
print("Original:", original_list)
print("Shallow :", shallow_copy)


# 2. DEEP COPY
"""
Deep copy duplicates both outer and inner objects.
"""

deep_copy = copy.deepcopy(original_list)

deep_copy[1][1] = 100

print("\nAfter modifying deep copy:")
print("Original:", original_list)
print("Deep    :", deep_copy)


# 3. REAL-WORLD EXAMPLE
"""
Copying user profile data with preferences.
"""

user_profile = {
    "name": "Bob",
    "preferences": ["dark_mode", "email_notifications"]
}

shallow_profile = copy.copy(user_profile)
deep_profile = copy.deepcopy(user_profile)

shallow_profile["preferences"].append("sms_alerts")

print("\nUser Profile:", user_profile)
print("Shallow Copy:", shallow_profile)
print("Deep Copy   :", deep_profile)
