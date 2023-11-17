student_scores = {
    "Ram": 81,
    "Shyam": 78,
    "Hari": 99,
    "Sita": 74,
    "Draco": 62
}

student_grades = {}
for student in student_scores:
    score = student_scores[student]
    if score>90 :
        student_grades[student] = "Outstanding"
    elif score>80:
        student_grades[student] ="Exceeds Expectation"
    elif score>70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"


print(student_grades)