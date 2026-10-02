#Read five student names and marks into a dictionary, calculate the average,
#identify the top student, and display all students above the average.
"""
   Step by step method
    Step 1. Start with an empty dictionary.
    Step 2. Repeat five times, reading a name and a numerical mark and storing them as a key-value pair.
    Step 3. Calculate average = sum of marks / number of students.
    Step 4. Find the key associated with the maximum value.
    Step 5. Loop through the dictionary again and display only marks greater than the average.

"""
students = {}

for count in range(5):
    name = input(f"Enter student {count + 1} name: ")
    mark = float(input(f"Enter {name}'s mark: "))
    students[name] = mark

average = sum(students.values()) / len(students)
top_student = max(students, key=students.get)

print(f"Class average: {average:.2f}")
print(
    f"Highest: {top_student} with {students[top_student]:.2f}"
)

print("Students above the average:")
for name, mark in students.items():
    if mark > average:
        print(f"{name}: {mark:.2f}")
