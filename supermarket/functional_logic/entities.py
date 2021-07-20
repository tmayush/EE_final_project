# Importing Helper Functions
from supermarket.helper_functions import random_functions
from supermarket.helper_functions import table

# Built in Modules - Python 3
import time

# Under development - generate_report
class Supermarket:
    def __init__(self, name, max_temperature, my_menu, id_list) -> None:
        self.name = name
        self.id = random_functions.gen_id(1, 100, id_list)
        self.max_temperature = float(max_temperature)
        self.people = []
        self.city = "Hyderabad"

        id_list.append(self.id)
        my_menu.my_admin.object_data["Supermarkets"][0].append(self)

    def number_of_people(self):
        return len(self.people)

    def add_person(self, person):
        # print("Person added to market")
        self.people.append(person)

    def temperature_check(self, temperature):
        return temperature < self.max_temperature

    def generate_report(self):
        report = {
            "Supermarket ID": self.id,
            "Name of the Supermarket": self.name,
            "Temperature Limit": self.max_temperature,
        }
        return report

    def counter(self, person):
        # access their bag
        # Show the bag
        # you will calculate their total amount and add taxes
        # youll ask them the total amount that they want to give
        # check for discounts
        pass

    def __str__(self) -> str:
        return self.name


# Under development - Products interaction, generate_report
class Person:
    def __init__(self, name, temperature, super_market, my_menu, id_list) -> None:
        self.id = random_functions.gen_id(1000, 9999, id_list)
        self.name = name
        self.temperature = float(temperature)
        self.super_market = super_market
        self.bag = []
        # self.bag = [
        #     ["Products", "Price", "Quantity"],
        #     ["Cofeee", "24", "1"],
        #     ["Hamburger", "2454", "2"],
        #     ["Pancakes", "44", "1"],
        # ]

        id_list.append(self.id)
        my_menu.my_admin.object_data["People"][0].append(self)

        self.my_menu = my_menu
        self.start_time = None
        self.end_time = None

    def time_elapsed(self):
        calc_time_elapsed = round(time.time() - self.start_time)
        print(f"Time Elapsed - {calc_time_elapsed} seconds\n")
        return calc_time_elapsed

    def enter_market(self):
        # self.super_market = super_market
        if self.super_market.temperature_check(self.temperature):
            print("Welcome\n")
            self.super_market.add_person(self)
            self.start_time = time.time()
            self.my_menu.state = "in_market"
        else:
            print("Sorry Not Allowed!")

    def check_bag(self):
        if len(self.bag) == 0:
            print("No items present\n")
            return None
        else:
            new_list = table.create_table(self.bag, 4)
            for line in new_list:
                final_line = ""
                for word in line:
                    final_line += f"|{word}"
                final_line += "|"
                print(final_line)
            print()
            return True

    def generate_report(self):
        report = {
            "Person ID": self.id,
            "Person Name": self.name,
            "Supermarket Name": self.super_market.name,
            "Items Present In Bag": str(self.bag),
            "Temperature": self.temperature,
        }
        if self.start_time is not None:
            report["Time Spent"] = str(round(time.time() - self.start_time))
        return report

    def __str__(self) -> str:
        return self.name

