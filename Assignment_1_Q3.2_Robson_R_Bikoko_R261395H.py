# Q.3.2 Python program that defines a Book class with a constructor to initialize the title, author,etc. price
class Book:
    def __init__(self, title, author, price):
       self.title = title
       self.author = author
       self.price = price

    # Method to display book details
    def display_details(self):
        print("Title :", self.title)
        print("Author:", self.author)
        print("Price : $", self.price)
        print()

# Instantiate two Book objects
book1 = Book("Python Programming", "John Smith", 29.99)
book2 = Book("Data Science Essentials", "Jane Doe", 39.99)

# Display book details
book1.display_details()
book2.display_details()
