# check whether the year is leap year or not
year = int(input("Enter the year: "))
if( year%4 ==0 and year % 100!=0):
    print("leap year")
else:
    print("Not a leap year")