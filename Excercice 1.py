#Here's a simple Python program that calculates an employee's pay,
#including overtime pay at 1.5 times the hourly rate for any hours worked over 40.
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

# Display the result
print("Gross Pay:", gross_pay)