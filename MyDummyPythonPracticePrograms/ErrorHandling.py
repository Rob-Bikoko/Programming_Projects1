def divide(a, b):
    try:
        # Attempt to perform the division
        result = a / b
        return result

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None

# Example usage
print(divide(10, 2))  # Performs division and returns result
print(divide(10, 0))  # Triggers a ZeroDivisionError