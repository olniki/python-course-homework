# 1. Modify the Country class to include a third instance attribute called capital as a string.
# Store your new class in a script and test it out by adding the following code at the bottom of the script:
# japan = Country('Japan', 140_000_000, 'Tokyo')
# print(f"{japan.name} population is {japan.population} and capital is {japan.capital}.")
# The output of your script should be:
# Japan population is 140000000 and capital is Tokyo.

# 2. Add increase_population method to country class.
# This method should take an argument and increase population of the country on this number.

# 3. Create add method to add two countries together.
# This method should create another country object with the name of the
# two countries combined and population of the two countries added together.

# 4.(Optional) Implement previous method with magic method
class Country:
    def __init__(self, name: str, population: int, capital: str = ''):
        self.name = name
        self.population = population
        self.capital = capital

    def increase_population(self, increase_by):
        self.population += increase_by

    def add_country(self, second_country):
        name = self.name + second_country.name
        population = self.population + second_country.population
        return Country(name, population)

    def __add__(self, second_country):
        name = self.name + second_country.name
        population = self.population + second_country.population
        return Country(name, population)


japan = Country('Japan', 140_000_000, 'Tokyo')
print(f"{japan.name} population is {japan.population} and capital is {japan.capital}.")
japan.increase_population(111)
print(f"{japan.name} population is {japan.population} and capital is {japan.capital}.")
bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

new_country = bosnia.add_country(herzegovina)
print(f"{new_country.name} population is {new_country.population}")

magic_country = bosnia+herzegovina
print(f"{magic_country.name} population is {magic_country.population}")
