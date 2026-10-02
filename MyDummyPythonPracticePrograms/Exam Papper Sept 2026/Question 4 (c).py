#Question 4c Minimum and maximum random floats
#Generate five random floating-point numbers from 0 to 10 and print the minimum and maximum.  [5 marks]
"""
    Step by step method
    Step 1. Call random.uniform(0, 10) five times in a list comprehension.
    Step 2. Pass the completed list to min() and max().
    Step 3. Display the generated list and the two results. Formatting to two decimal places improves readability without changing the stored values.

"""
import random

numbers = [random.uniform(0, 10) for _ in range(5)]

print("Generated values:")
for number in numbers:
    print(f"{number:.2f}")

print(f"Minimum: {min(numbers):.2f}")
print(f"Maximum: {max(numbers):.2f}")
