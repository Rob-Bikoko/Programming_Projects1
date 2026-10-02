#Create Student, DayStudent and BoardingStudent classes. Override calculate_fees(),
#store child objects in one list, and call the method polymorphically.
"""
   Key concepts
   •	Inheritance: DayStudent and BoardingStudent acquire the general identity of Student.
   •	Method overriding: each child class supplies its own calculate_fees() implementation.
   •	Polymorphism: the same expression student.calculate_fees() produces a result appropriate to the object's actual class.
   Step by step method
   Step 1. Define calculate_fees() in the parent class as a required operation.
   Step 2. Override it in DayStudent and return the tuition fee of $500.
   Step 3. Override it in BoardingStudent and return $500 tuition plus $300 boarding, giving $800.
   Step 4. Store one object of each child class in a common list.
   Step 5. Loop through the list and call calculate_fees() without using class-specific if statements.

"""
class Student:
    def calculate_fees(self):
        raise NotImplementedError("Subclasses must calculate fees.")


class DayStudent(Student):
    def calculate_fees(self):
        return 500


class BoardingStudent(Student):
    def calculate_fees(self):
        tuition_fee = 500
        boarding_fee = 300
        return tuition_fee + boarding_fee


students = [DayStudent(), BoardingStudent()]

for student in students:
    class_name = type(student).__name__
    print(f"{class_name} fees: ${student.calculate_fees()}")
