students = [
    {"name": "Rahim", "department": "CSE", "marks": 85, "attendance": 92},
    {"name": "Karim", "department": "CSE", "marks": 48, "attendance": 76},
    {"name": "Sara", "department": "DS", "marks": 91, "attendance": 95},
    {"name": "Nadia", "department": "DS", "marks": 67, "attendance": 84},
    {"name": "Hasan", "department": "CSE", "marks": 73, "attendance": 78}
]

def calculate_average(students):
    total = 0

    for student in students:
        total = total + student["marks"]

    average = total / len(students)
    return average

def highest_marks(students):
    highest = students[0]

    for student in students:
        if student["marks"] > highest["marks"]:
            highest = student

    return highest

def low_attendance(students):
    count = 0

    for student in students:
        if student["attendance"] < 80:
            count = count + 1

    return count


average = calculate_average(students)
top_student = highest_marks(students)
low_count = low_attendance(students)

print("Student Performance Summary: ")
print("Average marks:", average)
print("Highest-scoring student:", top_student["name"])
print("Highest marks:", top_student["marks"])
print("Students with attendance below 80%:", low_count)

