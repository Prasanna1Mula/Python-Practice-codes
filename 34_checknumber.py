def check_number(num):
    if num> 0:
        print("The number is a positive number")
    elif num< 0:
        print("The number is a negative number")
    else:
        print("Its zero")
def main():
    num = float(input("Enter a number: "))
    check_number(num)
if __name__ == "__main__": main()