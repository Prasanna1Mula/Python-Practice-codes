# Example 1 : User Authentication 
username= input("Enter your username: ")
password= input("Enter your password: ")

if username == "admin" and password == "12345":
    print("Login successful")
else:
    print("Login failed. Please check your credentials.")