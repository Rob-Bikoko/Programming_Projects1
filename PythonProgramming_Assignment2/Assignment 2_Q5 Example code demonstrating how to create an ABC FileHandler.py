# Example how to create an ABC FileHandler with abstract methods read() and write()
from abc import ABC, abstractmethod


# Abstract Base Class
class FileHandler(ABC):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass


# Concrete Class for Text Files
class TextFileHandler(FileHandler):

    def read(self):
        return "Reading text data..."

    def write(self, data):
        print(f"Writing text data: {data}")


# Concrete Class for Binary Files
class BinaryFileHandler(FileHandler):

    def read(self):
        return b"Reading binary data..."

    def write(self, data):
        print(f"Writing binary data: {data}")


# Create objects
text_handler = TextFileHandler()
binary_handler = BinaryFileHandler()

# Use methods
print(text_handler.read())
text_handler.write("Hello World")

print(binary_handler.read())
binary_handler.write(b"\x48\x65\x6C\x6C\x6F")