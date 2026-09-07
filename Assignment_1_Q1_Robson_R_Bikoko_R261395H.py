# Q.1 Python program that asks the user to enter their age
while True:
  try:
   age: int = int(input("Enter your age: "))
   break # Exit the loop if input is valid
  except ValueError:
   print("Invalid input. Please enter a valid integer.")

print(f"Your age is {age}.")





