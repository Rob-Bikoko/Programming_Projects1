# Q.2 Python program that list of favourite fruits
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

# Write fruits to the file
with open("fruits.txt", "w") as file:
  for fruit in fruits:
   file.write(fruit + "\n")

# Read and display the fruits from the file
with open("fruits.txt", "r") as file:
 for line in file:
  print(line.strip())
