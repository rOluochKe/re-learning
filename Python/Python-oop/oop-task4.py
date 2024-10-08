"""
Title: Travel Planner and Cost Calculator

Description:
The provided code represents a travel planning and cost calculation system. It allows you to input the country you want to travel to, the month of travel, and the type of trip (leisure or business). The system provides information about the trip and calculates the total cost based on flight expenses and additional costs.

#####

Let's understand how the code works:

1. Travel Planning:
When you create a new instance of the `Travel` class, you provide the country you want to visit, the month of travel, and the type of trip (leisure or business). The system stores this information.

2. Trip Information:
The `trip_info()` method provides information about your trip based on the month of travel. If the month falls between October and March, it considers it as a winter trip and displays a message stating the country and trip type (leisure or business). If the month is between April and September, it considers it as a summer trip and displays a similar message. If an invalid month is entered, it displays an error message.

3. Cost Calculation:
The `calc_cost(cost)` method calculates the total cost of the trip. It takes the flight cost as input and prompts you to enter any additional costs. The system keeps adding the costs and updates the total price accordingly. It also provides advice based on the total cost, categorizing it as "Low Budget" for costs below 500, "Enjoy a flight to anywhere!" for costs between 500 and 1500, and "Luxury trip!" for costs exceeding 1500.

4. Additional Cost Inspection:
The `list_inspection(costs)` method inspects the list of costs entered. It counts the number of costs that are equal to or greater than 10. If the count is less than or equal to 10, it increases the total price by 100 and displays an updated price.

#####

Outside the class, you can interact with the system by entering the country you want to visit, specifying the type of trip, and providing the month of travel. Then, you enter the flight cost and any additional costs. The system calculates the total cost, provides advice based on the cost, and performs an inspection on the list of costs to adjust the price if necessary.

This code helps you plan your travel, provides information about your trip, and calculates the cost based on flight expenses and additional costs.
"""


class Travel:
    def __init__(self, country, month, type):
        self.country = country
        self.month = int(month)
        self.type = type
        self.price = 0

    def trip_info(self):
        if self.month >= 10 and self.month <= 3:
            print(
                f"You are going to {self.country} in the Winter!  This is a {self.type} trip!")
        elif self.month > 3 and self.month < 10:
            print(
                f"You are going to {self.country} in the Summer!  This is a {self.type} trip!")
        else:
            print("Invalid Input!")

    def calc_cost(self, cost):
        costs = []
        while cost != 0:
            self.price += cost
            costs.append(cost)
            cost = int(input("Enter another cost: "))

        advice = self.advice(self.price)
        inspect = self.list_inspect(costs)
        return advice, inspect

    # depending on the value of self.price, advice given

    def advice(self, num):
        if num < 500:
            print("Low budget!")
        elif num >= 500 and num < 1500:
            print("Take a flight to anywhere...")
        else:
            print("Luxury Trip")

    # If list element < $10, add one
    # If counter > 10, add $100
    def list_inspect(self, costs):
        less_than_ten = 0
        for i in costs:
            if i <= 10:
                less_than_ten += 1

        if less_than_ten <= 10:
            self.price += 100
            print(f"Updated price: {self.price}")


location = input("Enter a country: ").capitalize()
trip_type = input("Leisure or Business: ").capitalize()
month = input("Enter a month: ")

test = Travel(location, month, trip_type)
test.trip_info()

flight_cost = int(input("Enter flight cost: "))
test.calc_cost(flight_cost)
