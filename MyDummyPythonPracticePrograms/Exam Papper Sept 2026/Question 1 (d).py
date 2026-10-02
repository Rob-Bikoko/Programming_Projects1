#Ask for the user's age, handle ValueError, and continue until
#the user supplies a valid integer
"""
   Step by step method
   Step 1. Use while True to create a loop that continues until the program explicitly exits it.
   Step 2. Read the user's input and pass it to int().
   Step 3. If conversion succeeds, display the age and use break to leave the loop.
   Step 4. If conversion fails, int() raises ValueError. Catch it and display a helpful message before the next loop iteration.

"""
while True:
    try:
        age = int(input("Enter your age: "))
        print("Your age is:", age)
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")
