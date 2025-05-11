# Defining the Car class
class Car:
    # Class variable (common to all instances)
    wheels = 4
    
    # Constructor to initialize object attributes
    def __init__(self, make, model, color, year):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
    
    # Method to display car details
    def displayCar(self):
        print(f"Car Make: {self.make}, Model: {self.model}, Wheels: {Car.wheels}, Color: {self.color}, Year: {self.year}")

# Creating objects of the Car class
car1 = Car("Toyota", "Corolla", "Black", "2022")
car2 = Car("Honda", "Civic", "Silver", "2023")

# Displaying car details
print("\nCar Details:")
car1.displayCar()
car2.displayCar()

# Thanking the user
print("\nThank you for using the car details program!")