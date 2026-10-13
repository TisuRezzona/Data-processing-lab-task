#Student Dictionary
student = {
    "name": "Tisma Reja",
    "id": "25-62393-2",
    "department": "DATA SCIENCE",
    "CGPA": 3.80
}

for key in student:
    print(key, ":", student[key])

if student["CGPA"] >= 2.50:
    print("Good Standing")
else:
    print("Academic Warning")
