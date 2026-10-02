#Question 4b Square list values with lambda and map
#Use a lambda function and map() to square every number in a list
#and print the new list.
"""
   Step by step method
   Step 1. Create a sample list.
   Step 2. Define the transformation inline as lambda number: number ** 2.
   Step 3. Pass the function and list to map(). map applies the function once to every item.
   Step 4. Convert the map object to a list so all transformed values can be displayed.

"""
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda number: number ** 2, numbers))

print("Original list:", numbers)
print("Squared list:", squares)
