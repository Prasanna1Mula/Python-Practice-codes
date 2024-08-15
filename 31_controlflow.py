# Continue Statement 
#processing a list, sipping invalid items 
numbers = [1,-2,3,0,4,5]
for num in numbers:
    if num<0:
        print("Invalid number, skipping:", num)
        continue
    print("Processing number:", num)