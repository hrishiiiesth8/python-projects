student_grades = {"Swati": 99, "Hrishit": 88}
for marks in student_grades:
    if student_grades[marks] > 90:
        print(f"{marks} = {student_grades[marks]} : Outstanding")
    elif student_grades[marks] < 90:
        print(f"{marks} = {student_grades[marks]} : Poor")
 