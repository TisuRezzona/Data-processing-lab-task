name = input("Enter passenger name: ")
destination = input("Enter destination: ")
ticket_count = int(input("Enter number of tickets: "))
passenger_type = input("Enter passenger type (adult/child/student/senior): ")


if destination == "Dhaka":
    fare = 500
elif destination == "Chittagong":
    fare = 800
elif destination == "Sylhet":
    fare = 600
else:
    fare = 1000

if passenger_type == "child":
    discount = 0.50
elif passenger_type == "student":
    discount = 0.20
elif passenger_type == "senior":
    discount = 0.30
else:
    discount = 0


fare_after_discount = fare - (fare * discount)
total_fare = fare_after_discount * ticket_count

print("Passenger:", name)
print("Destination:", destination)
print("Passenger Type:", passenger_type)
print("Number of Tickets:", ticket_count)
print("Fare per Ticket:", fare)
print("Discount:", discount * 100, "%")
print("Total Fare:", total_fare)
