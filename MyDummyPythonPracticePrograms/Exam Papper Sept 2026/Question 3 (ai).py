#Question 3a Part i Student marks dictionary
#Create a dictionary for five students, display every student and mark,
#and find the highest-scoring student
#Step by step method
#Step 1. Use student names as dictionary keys and marks as dictionary values.
#Step 2. Loop through students.items() to obtain each name and mark.
#Step 3. Use max(students, key=students.get). This compares keys according to their associated mark values.
#Step 4. Use the returned name to obtain and display the highest mark.
students = {
    "Tendai": 78,
    "Rudo": 85,
    "Brian": 69,
    "Nyasha": 92,
    "Farai": 74,
}

for name, mark in students.items():
    print(f"{name}: {mark}")

top_student = max(students, key=students.get)
print("Highest-scoring student:", top_student)
print("Highest mark:", students[top_student])
