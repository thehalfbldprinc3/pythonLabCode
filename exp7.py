class Car:
    wheels=4
    def __init__(self, make, model, color, year):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
    def displayCar(self):
        print(f"Car Make: {self.make}, Model: {self.model}, Wheels: {Car.wheels}, Color: {self.color} Year: {self.year}")

car1= Car("Toyota", "Corolla", "Black", "2022")
car2= Car("Honda", "Civic", "Silver", "2023")

car1.displayCar()
car2.displayCar()