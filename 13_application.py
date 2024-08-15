# Temperature converter 

while True:
    print("Menu: ")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenhiet to Celsius")
    print("3.Exit")
    choice = int(input("Ente your choice: "))
    if choice == 1:
        celsius = float(input("Enter temperature in celsius: "))
        fahrenhiet = (celsius *9/5)+ 32
        print("Temperature in Fahrenhiet:" , fahrenhiet)
    elif choice == 2:
        fahrenhiet = float(input("Enter temperature in fahrenhiet: "))
        celsius = (fahrenhiet-32)*5/9
        print("Temperature in Celsius:", celsius)
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice. please select again.")