
def get_positive_number():
    number = -1  # Initialize with a negative number
    while number < 0:
        number = float(input("Please enter a positive number: "))
    return number

# Example usage
positive_number = get_positive_number()
print(f"You entered: {positive_number}")