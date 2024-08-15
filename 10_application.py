#percentage score calculator 
percentage = float(input("Enter percentage score: "))
if percentage >= 90:
    print("Grade: A")
elif percentage >= 80:
    print("Grade: B")
elif percentage >= 70:
    print("Grade: C")
elif percentage >=60:
    print("Grade: D")
else:
    print("Grade: F")