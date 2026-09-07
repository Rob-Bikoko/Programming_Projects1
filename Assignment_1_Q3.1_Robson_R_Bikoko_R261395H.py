# Q.3  Dictionary of students and their marks
students = {
"Alice": 85,
"Brian": 92,
"Cynthia": 78,
"David": 95,
"Emma": 88
}

# Q.3.1 Python program that display all students and their marks
print("Students and their marks:")
for student, mark in students.items():
    print(f"{student}: {mark}")

# Find the student with the highest mark
   highest_student = max(students, key=students.get)
   highest_mark = students[highest_student]

print("\nStudent with the highest mark:")
print(f"{highest_student} with {highest_mark} marks")
