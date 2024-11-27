def is_equilateral(a, b, c):
    if a == b and b == c and c == a :
        return "Yes"
    else:
        return "No"
    

def main():
    # Input the lengths of the triangle sides

     a = int(input("Enter the length of the first side of the triangle: "))
     b = int(input("Enter the length of the second side of the triangle: "))
     c = int(input("Enter the length of the third side of the triangle: "))

        # Check if the triangle is equilateral
     result = is_equilateral(a, b, c)
     print(f"Is the triangle equilateral? {result}")


main()