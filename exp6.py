# Importing the math library
import math as m

# Function to calculate the area of a circle
def areaOfCircle(radius):
    area = m.pi * radius**2
    return area

# Taking user input
try:
    radius = float(input("Enter the radius of the circle: "))
    if radius < 0:
        print("Radius cannot be negative. Please enter a valid value.")
    else:
        # Calling the function and displaying the result
        print(f"The area of the circle with radius {radius} is: {areaOfCircle(radius):.2f}")
except ValueError:
    print("Invalid input! Please enter a numeric value.")

# Thanking the user
print("\nThank you for using the circle area calculator!")