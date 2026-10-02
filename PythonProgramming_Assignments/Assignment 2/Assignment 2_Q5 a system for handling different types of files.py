#Q5. Scenario: You are designing a system for handling different types of files.
# You want to ensure that all file handler classes implement certain essential methods,
# such as read() and write().
# Provide example code demonstrating how to create an ABC FileHandler with abstract
#methods read() and write(), and how to create concrete classes like TextFileHandler
#and BinaryFileHandler that inherit from FileHandler.
"""
   To ensure that all file handler classes implement required methods such as read()
   and write(), Python provides the Abstract Base Class (ABC) mechanism through the abc
   module.
   An abstract class acts as a blueprint. Any class that inherits from it must implement
   all abstract methods, otherwise Python will prevent that class from being instantiated.

"""
from abc import ABC, abstractmethod

# Abstract Base Class
class FileHandler(ABC):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass


# Concrete Class for handling text files
class TextFileHandler(FileHandler):

    def read(self):
        print("Reading data from a text file.")

    def write(self, data):
        print(f"Writing '{data}' to a text file.")


# Concrete Class for handling binary files
class BinaryFileHandler(FileHandler):

    def read(self):
        print("Reading data from a binary file.")

    def write(self, data):
        print(f"Writing '{data}' to a binary file.")


# Create objects
text_file = TextFileHandler()
binary_file = BinaryFileHandler()

# Use the methods
text_file.read()
text_file.write("Hello World")

binary_file.read()
binary_file.write(b'101010')