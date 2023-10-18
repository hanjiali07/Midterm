import random
userName = input("Please enter your name: ")
print("Hi",userName,",welcome to House Value Calculator:")

print("Select the City")
print("1 Toronto")
print("2 Montreal")

selection = int(input("Enter your selection:"))
getArea = int(input("Enter the area:"))
getRooms = int(input("Enter number of rooms:"))


if selection == 1:
    print("You have selected the city of Toronto.")
   
    if getArea < 0:
        print("Area must be greater than 0.")
        a = int(input("Please enter the area:"))
        print("Area:", getArea)
    else:
        print("Area:",getArea)

    if getRooms < 0 or getRooms > 5:
        print("Number of rooms has to be between 1 and 5.")
        b = int(input("Please enter number of rooms:"))
        print("Number of rooms:",getRooms)
    else:
        print("Number of rooms:",getRooms)
    def estimatedPriceToronto():
        import toronto
        a = toronto.results
        b = getRooms
        return a * b
    print("Hi",userName)
    print("House value calculator.")
    print("House information: Toronto,","Area,",getArea,",","Number of rooms:",getRooms )
    print("Estimated price of house:" ,estimatedPriceToronto())
else:
    print("You have selected Montreal.")
    if getArea < 0:
        print("Area must be greater than 0.")
        a = int(input("Please enter the area:"))
        print("Area:", getArea)
    else:
        print("Area:",getArea)

    if getRooms < 0 or getRooms > 5:
        print("Number of rooms has to be between 1 and 5.")
        b = int(input("Please enter number of rooms:"))
        print("Number of rooms:",getRooms)
    else:
        print("Number of rooms:",getRooms) 
    def montrealPrice():
        x = random.randint(250, 550)
        result = x * 900
        rooms = result * getRooms
        return rooms 
    print("Estimated price of house:", montrealPrice())
