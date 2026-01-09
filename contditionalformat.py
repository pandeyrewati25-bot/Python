# ATM CONDITION
balance = 100
withdraw = int(input("Enter amount to withdraw"))

if withdraw <= balance :
    print("Transaction Successful:")

else:
    print("Low balance")

#Attendence
Time = float(input("Enter your arrival time(12-hour format, e.g., 09.00 or 9.30): "))

if Time <= 9.00:
    print("On Time - Present")
elif Time >= 9.20 :
    print("late - present")
else:
    print("absent")

# idetify Vechile

# vechile =input("Enter vechile name: ")

# if vechile in ("Bike", "Scooter", "Activa", "Splendor", "Bullet"):
#     print("This is a 2 wheeler vechile.")
# elif vechile in ("Car", "Bus", "Swift", "Bolero", "Ambulance"):
#     print("This is a 4 wheeler vehicle.")
# else:
#     print("Unknown vehicle type.")