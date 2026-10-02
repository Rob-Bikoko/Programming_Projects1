#Question 2bi Part i Multiplication table
#Display the multiplication table, from 1 to 12, of a number entered by the user
'''
   Step by step method
   Step 1. Read the number and convert it to an integer.
   Step 2. Use range(1, 13) because 13 is excluded, producing the multipliers 1 through 12.
   Step 3. For each multiplier, calculate number * multiplier.
   Step 4. Use an f-string to display the multiplication statement and product.

'''

number = int(input("Enter a number: "))

for multiplier in range(1, 13):
    product = number * multiplier
    print(f"{number} x {multiplier} = {product}")

