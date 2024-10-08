"""
Story Description:

In a world where transportation is evolving, there exists a class called "Vehicle" that represents a generic vehicle with attributes such as make, model, and year.

#####

In parallel, there are two specialized classes, namely "ElectricVehicle" and "GasolineVehicle."

The "ElectricVehicle" class focuses on vehicles powered by electricity and includes features like battery capacity and the ability to charge.

The "GasolineVehicle" class, on the other hand, deals with vehicles powered by gasoline and includes attributes like fuel capacity and the ability to refuel.

***Both of these classes also have a method called "get_range" which calculates the range of the vehicle based on their respective energy sources.

###

Now, imagine a futuristic hybrid car called "HybridCar" that combines the features of an electric vehicle and a gasoline vehicle.

-This class inherits from the "Vehicle," "ElectricVehicle," and "GasolineVehicle" classes. By leveraging multiple class inheritance, the "HybridCar" class brings together the capabilities of both electric and gasoline-powered vehicles into a single entity.

#####

Outside your classes, we create an object of the "HybridCar" class, specifically a Toyota Prius model from 2022. The car is equipped with a battery capacity of 5.5 kWh and a fuel capacity of 40 gallons. The "HybridCar" class utilizes the initialization methods of its parent classes to set up the vehicle attributes.

To showcase the car's functionality, we call the "charge" method to obtain the battery capacity, the "refuel" method to get the fuel capacity, and the "get_range" method to calculate the battery and fuel range.

The range is calculated by assuming that 1 unit of battery capacity provides 5 miles of range, and 1 unit of fuel capacity offers 20 miles of range.

Finally, we print out the obtained values of battery capacity, fuel capacity, battery range, and fuel range to display the capabilities of the hybrid car.

This code shows the concept of multiple class inheritance in the context of a hybrid car, showcasing the integration of electric and gasoline vehicle features into a single vehicle model
"""


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


class ElectricCar:
    def __init__(self, battery_capacity):
        self.battery_cap = battery_capacity

    def charge(self):
        return self.battery_cap

    def get_range(self):
        return self.battery_cap * 5


class GasCar:
    def __init__(self, fuel_capacity):
        self.fuel_cap = fuel_capacity

    def refuel(self):
        return self.fuel_cap

    def get_fuel_range(self):
        return self.fuel_cap * 20


class Hybrid(Vehicle, ElectricCar, GasCar):
    def __init__(self, make, model, year, battery_capacity, fuel_capacity):
        Vehicle.__init__(self, make, model, year)
        ElectricCar.__init__(self, battery_capacity)
        GasCar.__init__(self, fuel_capacity)


car = Hybrid("Toyota", "Prius", 2023, 5, 40)

battery_capacity = car.charge()
fuel_cap = car.refuel()
battery_range = car.get_range()
fuel_range = car.get_fuel_range()

print(f"Battery Capacity: {battery_capacity} kWh")
print(f"Fuel Capacity: {fuel_cap} gallons")
print(f"Battery Range: {battery_range} miles")
print(f"Fuel Range: {fuel_range} miles")
