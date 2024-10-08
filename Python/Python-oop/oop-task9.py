"""
Title: Country Information System

country = {}

country[key] = value

dictionary -> key -> unlocks a value

Description:
The provided code represents a country information system that allows users to retrieve information about different countries. The system is built using class inheritance to categorize countries into two types: developed and developing.

#####

Country Class:
The base class `Country` represents a generic country and stores its name, capital, and population.

-It provides a method `get_info()` that returns a dictionary containing the country's name, capital, and population.

###

DevelopedCountry Class:
The `DevelopedCountry` class inherits from the `Country` class and adds an additional attribute `gdp` (Gross Domestic Product).

-It overrides the `get_info()` method to include the GDP in the returned dictionary.

###

DevelopingCountry Class:
The `DevelopingCountry` class also inherits from the `Country` class and introduces the attribute `hdi` (Human Development Index).

-It overrides the `get_info()` method to include the HDI in the returned dictionary.

###

World Class:
The `World` class serves as a container for multiple countries.

-It allows the addition of countries with add_country(country) and provides a method `get_country_info()` to retrieve the information for a specific country by its name.

#####

Outside your classes, an instance of the `World` class named `world` is created. Three countries, namely the United States, India, and China, are instantiated as objects of their respective classes and added to the `world` instance.

To retrieve information about a specific country, the `get_country_info()` method is used with the country name as an argument. If the country is found in the `world` instance, its information is displayed. Otherwise, a message indicating that the country was not found is printed.

This code allows users to organize and access information about countries based on their development status. It facilitates the retrieval of data such as the country's name, capital, population, and additional attributes specific to developed or developing countries.
"""


class Country:
    def __init__(self, name, capital, population):
        self.name = name
        self.capital = capital
        self.pop = population

    def get_info(self):
        return {
            "Name": self.name,
            "Capital": self.capital,
            "Population": self.pop
        }


class DevelopedCountry(Country):
    def __init__(self, name, capital, population, gdp):
        super().__init__(name, capital, population)
        self.gdp = gdp

    def get_info(self):
        info = super().get_info()
        info["GDP"] = self.gdp
        return info


class DevelopingCountry(Country):
    def __init__(self, name, capital, population, hdi):
        super().__init__(name, capital, population)
        self.hdi = hdi

    def get_info(self):
        info = super().get_info()
        info["HDI"] = self.hdi
        return info


class World:
    def __init__(self):
        self.countries = []

    def add_country(self, country):
        self.countries.append(country)

    def get_country_info(self, name):
        for country in self.countries:
            if country.name == name:
                return country.get_info()
        return None


world = World()

usa = DevelopedCountry(
    "United States", "Washington, D.C.", 331000000, 22512000)
india = DevelopingCountry("India", "New Delhi", 1380004385, 0.645)
china = DevelopingCountry("China", "Beijing", 1444216107, 0.758)

world.add_country(usa)
world.add_country(india)
world.add_country(china)

country_info = world.get_country_info('United States')

if country_info:
    print("Country Info: ")
    for key, value in country_info.items():
        print(f'{key}:{value}')
else:
    print("Country not found!")
