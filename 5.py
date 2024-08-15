#find the largest among the three numbers 
num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))
num3 = int(input("Enter the number: "))

if num1>= num2 and num1>=num3:
    print("Num1 is the largest")
elif num2>= num1 and num2>= num3:
    print("Num2 is the largest")
else:
    print("Num3 is the largest")