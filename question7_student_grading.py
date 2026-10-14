
students = {
    "Ali": 85,
    "Ayesha": 92,
    "Sara": 76,
    "Ahmed": 65,
    "Hina": 88
}

for name, marks in students.items():

    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    else:
        grade = "F"

    print(name, "Marks:", marks, "Grade:", grade)
