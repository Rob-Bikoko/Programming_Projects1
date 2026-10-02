def determine_grade(score):
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    return grade


# Example usage
score = 65
print(f"The grade for a score of {score} is: {determine_grade(score)}")  # Output: B