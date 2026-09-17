#Rewrite your pay program using try and except so that your program handles
#non-numeric input
try:
    # Get input from the user
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter hourly rate: "))

    # Calculate pay
    if hours > 40:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * (rate * 1.5)
        gross_pay = regular_pay + overtime_pay
    else:
        gross_pay = hours * rate

    # Display result
    print("Gross Pay:", gross_pay)

except ValueError:
    print("Error: Please enter numeric values for hours and rate.")