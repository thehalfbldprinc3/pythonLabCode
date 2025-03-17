import math as m

def areaOfCircle(radius):
    area= 2 * m.pi * radius

    return area

radius=float(input("Enter the radius of the circle: "))

print("The area of the circle is: ", areaOfCircle(radius))