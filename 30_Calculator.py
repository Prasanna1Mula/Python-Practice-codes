def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y== 0:
        return "Error: Division by zero"
    return x/y
num1 = 10
num2 = 5
print("Addition:", add(num1, num2))
print("Subraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))