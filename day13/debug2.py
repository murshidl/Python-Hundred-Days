# def odd_or_even(number):
#     if number % 2 = 0:
#         return "This is an even number."
#     else:
#         return "This is an odd number."



def odd_or_even(number):
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."
    
print(odd_or_even(5))

# Bug Report: odd_or_even Function

# Issue:

# The if condition uses = (assignment) instead of == (comparison), which causes a SyntaxError.

# Cause:

# In Python, = assigns a value, while == checks equality. Using = in a condition is invalid.

# Solution:

# Replace = with == in the if condition.