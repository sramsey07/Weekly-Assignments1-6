x = int(input("Enter the first side: "))
y = int(input("Enter the second side: "))
z = int(input("Enter the third side: "))

if ((x*x + y*y == z*z) or (y*y + z*z == x*x) or (z*z + x*x ==y*y)):
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")
