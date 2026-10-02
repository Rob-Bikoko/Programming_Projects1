#Question 1e Write and read favourite fruits
#Store five fruits in fruits.txt, one per line, then read and display them.
#Use with for every file operation.
"""
   Step by step method
   Step 1. Create a Python list containing five fruit names.
   Step 2. Open fruits.txt in write mode. The with statement closes the file automatically.
   Step 3. Write each fruit followed by a newline character so every item occupies a separate line.
   Step 4. Open the same file in read mode.
   Step 5. Loop through the file and display each line after removing its trailing newline with strip().

"""
fruits = ["Mango", "Banana", "Orange", "Apple", "Guava"]

with open("fruits.txt", "w", encoding="utf-8") as file:
    for fruit in fruits:
        file.write(fruit + "\n")

with open("fruits.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
"""
    After the first with block, the file contains five lines. 
    The second with block reads the file sequentially. 
    Using with prevents a file from remaining open when an exception occurs.
"""