#4.	Write a Python program that uses the random module to generate a list of 5
#random floating-point numbers between 0 and 10
import random

# Generate a list of 5 random floating-point numbers between 0 and 10
numbers = [random.uniform(0, 10) for _ in range(5)]

# Print the generated list

print("Random numbers:", numbers)

# Find and print the minimum and maximum values

print("Minimum value:", min(numbers))

print("Maximum value:", max(numbers))