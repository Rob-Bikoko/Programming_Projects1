#Question 3a Part ii Book class
#Create Book with title, author and price attributes, add a display method,
#and instantiate two objects.
#Step by step method
#Step 1. Define the class with the class keyword.
#Step 2. Define __init__ as the constructor. self refers to the object being created.
#Step 3. Store the supplied title, author and price in instance attributes.
#Step 4. Define display_details() to print the state of one Book object.
#Step 5. Instantiate two independent objects and call the method on each.
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price:.2f}")


book1 = Book("Python Basics", "A. Moyo", 25.00)
book2 = Book("Database Systems", "T. Ncube", 32.50)

book1.display_details()
print()
book2.display_details()
