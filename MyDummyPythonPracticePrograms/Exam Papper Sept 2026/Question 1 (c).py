#Calculate an average using args
#Implement calculate_average using *args and return the arithmetic mean of the supplied numbers.
#Include a docstring
"""" Step by step method
     Step 1. Collect the supplied values in the args tuple.
     Step 2. Reject an empty tuple because division by zero would occur when calculating the average.
     Step 3. Use sum(args) to obtain the total of all values.
     Step 4. Use len(args) to obtain the number of values.
     Step 5. Divide the total by the count and return the result.
"""
def calculate_average(*args):
    """Calculate and return the arithmetic mean of supplied numbers.

    Parameters:
        *args: A variable number of integer or floating-point values.

    Returns:
        float: The arithmetic mean of the supplied values.

    Raises:
        ValueError: If no values are supplied.
    """
    if not args:
        raise ValueError("At least one number is required.")

    return sum(args) / len(args)


print("Average:", calculate_average(10, 20, 30, 40))
