#Question 2d Custom negative number exception
#Define NegativeNumberError, raise it when a number is negative,
#and demonstrate the function in a try block
"""
   Step by step method
   Step 1. Create a new exception class that inherits from Exception.
   Step 2. In check_positive(), test whether the number is below zero.
   Step 3. Use raise NegativeNumberError(...) when the test is true.
Step 4. Call the function inside try and catch NegativeNumberError with except.

"""
class NegativeNumberError(Exception):
    """Raised when a negative number is supplied."""


def check_positive(number):
    if number < 0:
        raise NegativeNumberError(
            f"{number} is negative; a non-negative value is required."
        )
    return number


try:
    value = check_positive(-8)
    print("Accepted value:", value)
except NegativeNumberError as error:
    print("Error:", error)
