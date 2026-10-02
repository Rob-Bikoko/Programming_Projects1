#Question 1a Find the maximum value using args
#Define find_maximum so that it accepts any number of numerical arguments
# through *args, returns the largest value and contains a suitable docstring.
"""Return the largest number supplied to the function.
  Parameters:
      *args: A variable number of integer or floating-point values.
  Returns:
      The largest supplied value.
  Raises:
      ValueError: If no values are supplied.
"""
""" Step by step method
    Step 1. Use *args in the function header. Python collects all supplied positional arguments into a tuple named args.
    Step 2. Check whether the tuple is empty. A maximum cannot be calculated when no numbers are supplied.
    Step 3. Apply Python's max() function to the tuple.
    Step 4. Return the largest value to the caller. The caller may store or print the returned value.
"""

def find_maximum(*args):

    if not args:
        raise ValueError("At least one number is required.")

    return max(args)

answer = find_maximum(12, 5, 28, 9)
print("Largest value:", answer)
