import math

# Step 1: Get the three sides from the user
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Error: Side lengths must be positive numbers.")
elif (a + b <= c) or (a + c <= b) or (b + c <= a):
    print("Error: The given sides do not form a valid triangle.")
else:
    s = (a + b + c) / 2  # Semi-perimeter
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("Area of the triangle:", area)