#Question 2c Division with exception handling
#Create divide_numbers(numerator, denominator), handle ZeroDivisionError and TypeError,
#return a valid result, and print suitable error messages.
"""
   Step by step method
   Step 1. Place numerator / denominator inside a try block.
   Step 2. A denominator of zero raises ZeroDivisionError; catch it and explain the problem.
   Step 3. An unsupported operand, such as a string divided by a number, raises TypeError; catch it separately.
   Step 4. Use else to return the result only when no exception occurred.

"""
def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("Error: division by zero is not allowed.")
        return None
    except TypeError:
        print("Error: numerator and denominator must be numbers.")
        return None
    else:
        return result


print(divide_numbers(20, 4))
divide_numbers(20, 0)
divide_numbers("20", 4)
