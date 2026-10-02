def file_operations(filename, mode, content=None):
    """
    Performs file operations (read, write, append) based on the given mode.

    Args:
        filename (str): The name of the file to operate on.
        mode (str): The mode in which to open the file ('r', 'w', 'a').
        content (str, optional): The content to write or append to the file. Defaults to None.

    Returns:
        str or None: The content read from the file if mode is 'r', otherwise None.
        bool: True if file operation successful, False otherwise.
    """
    try:
        if mode == 'r':
            with open(filename, 'r') as file:
                return file.read(), True
        elif mode == 'w':
            with open(filename, 'w') as file:
                if content is not None:
                    file.write(content)
                return True
        elif mode == 'a':
            with open(filename, 'a') as file:
                if content is not None:
                    file.write(content)
                return True
        else:
            print("Invalid mode. Use 'r', 'w', or 'a'.")
            return False

    except FileNotFoundError:
        print(f"File not found: {filename}")
        return False, False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False, False

# Example usage:
"""
    Purpose: Creates a new file or truncates an existing file to zero length.
    Behavior: If the file already exists, all existing content is deleted, and new data is written from the beginning.
    Usage: Use this mode when you want to start fresh with the file content.
"""
# Writing to a file
write_success = file_operations("file.docx", "w", "Hie, world!\nThis is a sample file.")
if write_success:
  print("Write successful")


"""
    Purpose: Opens an existing file and adds new content at the end of the file without truncating it.
    Behavior: If the file does not exist, it creates a new one. Existing content remains intact.
    Usage: Use this mode when you want to add data to a file without losing the existing content.
"""
# Appending to a file
append_success = file_operations("file.docx", "a", "\nAppending some more text.")
if append_success:
    print("Append successful")

# Reading from a file
read_content, read_success = file_operations("file.docx", "r")
if read_success:
    print("File content:")
    print(read_content)

#Handling File not found
not_found, success = file_operations("file.docx", "r")

#Example of binary mode
def binary_file_operations(filename, mode, data=None):
    try:
        if mode == 'rb':
            with open(filename, 'rb') as file:
                return file.read(), True
        elif mode == 'wb':
            with open(filename, 'wb') as file:
                if data is not None:
                    file.write(data)
                return True
        else:
            print("Invalid binary mode. Use 'rb', or 'wb'.")
            return False

    except FileNotFoundError:
        print(f"File not found: {filename}")
        return False, False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False, False

#Example of using binary mode.
binary_data = b'\x00\x01\x02\x03' #Example binary data
binary_write_success = binary_file_operations("binary_file.bin", "wb", binary_data)

if binary_write_success:
    print("binary write successful")
binary_read_data, binary_read_success = binary_file_operations("binary_file.bin", "rb")

if binary_read_success:
    print("Binary read successful")
    print(binary_read_data)