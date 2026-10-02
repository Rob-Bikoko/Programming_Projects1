#Generate 10 random integers between 1 and 100, then calculate and print their average
#Step by step method
#Step 1. Import the random module.
#Step 2. Use a list comprehension that calls random.randint(1, 100) exactly 10 times. Both 1 and 100 may be generated.
#Step 3. Calculate the total using sum(numbers).
#Step 4. Divide by len(numbers), which is 10.
import random

numbers = [random.randint(1, 100) for _ in range(10)]
average = sum(numbers) / len(numbers)

print("Generated numbers:", numbers)
print("Average:", average)
