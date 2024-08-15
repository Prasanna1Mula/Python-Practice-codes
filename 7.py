# check if a number is palindrome 
num = int(input("Enter the number: "))
temp = num 
reverse_num = 0
while temp> 0:
    digit = temp% 10
    reverse_num = reverse_num*10 + digit
    temp //= 10
if num== reverse_num:
    print("Palindrome")
else:
    print("Not a Palindrome")