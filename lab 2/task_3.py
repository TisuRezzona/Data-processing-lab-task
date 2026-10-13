# Weekend Temperature with a Tuple

temperatures = (28, 30, 29, 28, 31, 27)

print("Recorded temperatures:")

for temp in temperatures:
    print(temp)

highest = max(temperatures)
lowest = min(temperatures)

print("Highest temperature:", highest, "°C")
print("Lowest temperature:", lowest, "°C")
