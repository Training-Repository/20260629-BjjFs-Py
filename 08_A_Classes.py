
class Car:
    # Class variable
    total_cars = 0

    # def __new__(cls):
    #     pass

    @staticmethod
    def GenSerial():
        from random import randint
        return randint(100, 999)    

    def __init__(self, make, model, year, color):
        # Instance variables
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.serial = self.GenSerial()
        # Increment the total number of cars
        self.total_cars += 1

    @classmethod
    def car_count(cls):
        # Class method to access class variable
        return cls.total_cars

    def start(self):
        # Instance method
        print(f"{self.year} {self.make} {self.model} is starting.")

    @staticmethod
    def about():
        # Static method
        return "This is a car class."

    def __str__(self):
        # Method overriding for string representation
        return f"{self.year} {self.color} {self.make} {self.model} {self.serial}"

    def __add__(self, other):
        # Operator overloading for addition
        return f"{self.make} {self.model} and {other.make} {other.model}"


# Create instances of the Car class
car1 = Car("Toyota", "Camry", 2022, "Blue")
car2 = Car("Honda", "Accord", 2022, "Red")

# Call instance methods
car1.start()
car2.start()
# car1.__class__.__name__

# Access class method
print("Total Cars:", Car.car_count())

# Call static method
print(Car.about())

# Display car information using __str__ method
print(car1)
print(car2)

car1.engine = "v6"
delattr(car1, "model")
print(car1)

print(f"{car1.engine = }")
print(f"{car2.engine = }")

# Demonstrate operator overloading
print(car1 + car2)