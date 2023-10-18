userName = input("Please enter your name: ")
print("Hi",userName,",welcome to House Value Calculator:")

print("Select the City")
print("1 Toronto")
print("2 Montreal")

selection = int(input("Enter your selection:"))
getArea = int(input("Enter the area:"))
getRooms = int(input("Enter number of rooms:"))


if selection == 1:
    print("You have selected Toronto.")
else:
    print("You have selected Montreal.")

if getArea < 0:
    print("Area must be greater than 0.")
    a = int(input("Please enter the area:"))

if getRooms < 0 or getRooms > 5:
    print("Number of rooms has to be between 1 and 5.")
    b = int(input("Please enter number of rooms:"))

