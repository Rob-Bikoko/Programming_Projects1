#Question 2bii Part ii Examination grade
#Read an examination score and display A for 80-100, B for 70-79, C for 60-69,
#D for 50-59, and F for a score below 50
"""
     Step by step method
     Step 1. Read and convert the score to a floating-point number.
     Step 2. First reject scores outside the valid interval 0 to 100.
     Step 3. Test the valid score from the highest boundary downward. Once a condition is true, the remaining elif branches are skipped.
     Step 4. Display the selected grade.

"""
score = float(input("Enter examination score: "))

if score < 0 or score > 100:
    print("Invalid score. Enter a value from 0 to 100.")
elif score >= 80:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
elif score >= 50:
    print("Grade: D")
else:
    print("Grade: F")
