#Student performance analyzer
name = str(input("Enter student's name: "))
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter mark for course {i}: "))
    marks.append(mark)

total = sum(marks)
average = total/5
highest_mark = max(marks)
lowest_mark = min(marks)

passed = 0
for mark in marks:
    if mark >= 50:
        passed += 1


if average >= 80:
    performance = "Excellent"
elif average>= 70:
    performance = "Good"
elif average>= 60:
    performance = "Satisfactory"
elif average>= 50:
    performance = "Pass"
else:
    performance = "Needs Improvement"

print("Student Name: ",name)
print("Total Mark: ",total)
print("Average Mark: ",average)
print("Highest Mark: ",highest_mark)
print("Lowest Mark: ",lowest_mark)
print("Passed courses: ", passed)
print("Performance: ", performance)
