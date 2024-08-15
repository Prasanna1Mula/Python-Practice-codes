def calculate_rectangle_area(width,length):
    return width*length

def main():
    while True:
      length = float(input("Enter the length of rectangle: "))
      width = float(input("Enter the width of rectnagle: "))
      if length <= 0 or width <=0:
       print("The length and width must be positive,")
      else:
         area = calculate_rectangle_area(length, width)
         print(f"The area of the rectangle is the (area)")
         break 
    except ValueError: print("Invalid input. Please enter valid number.")
    if __name__ == "__main__": main()


      
