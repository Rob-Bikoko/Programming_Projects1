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