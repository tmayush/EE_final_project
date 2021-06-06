# supermarket = sp or market
from random_functions import *
from input_validation import handle_input
import time

people = []
people_ids = []
supermarkets = []
sp_ids = []
object_data = {"People": [people, people_ids], "Supermarkets": [supermarkets, sp_ids]}
# global_states = {
#     "global": [
#         {"1": "Create Supermarket"},
#         {"2": "Create Person"},
#         {"3": "Choose Supermarket"},
#         {"4": "Choose Person"},
#     ]
# }
# ------------Development --------
# def sc_market():
#     name = "iop"
#     return name


# def jkk(id):
#     return global_states[id]


# global_states = {
#     "global": [
#         {"Create Supermarket": jkk("Create Supermarket")},
#         {"Create Person": jkk("Create Person")},
#         {"Choose Supermarket": jkk("Choose Supermarket")},
#         {"Choose Person": jkk("Choose Person")},
#     ],
#     "Create Supermarket": sc_market,
# }
# print(type(jkk))
# ------------/Development --------

# global_states = {
#     "global": [
#         "Create Supermarket",
#         "Create Person",
#         "Choose Supermarket",
#         "Choose Person",
#     ]
# }

# products = ["Milk", "Cerial"]
# products = {"Dairy": ["Milk"],"Fasion":[]}
# States that a person can have:
# - out_market = the person is outside the market
# - in_market = the person is in market but not doing anythin
# - scanning_products = the person is in the products menu where all the available products are displayed properly
# - at_counter = the person is at the counter and entering the proper details to get their receipt


class Supermarket:
    # def __init__(self,current_time,opening_time,closing_time,max_temperature) -> None:
    def __init__(self, name, max_temperature, id_list=sp_ids) -> None:
        # self.current_time = current_time
        # self.opening_time = opening_time
        # self.closing_time = closing_time
        self.name = name
        self.id = gen_id(1, 100, id_list)
        object_data["Supermarkets"][0].append(self)
        self.max_temperature = float(max_temperature)
        self.people = []

    def number_of_people(self):
        return len(self.people)

    def add_person(self, person):
        print("Person added to market")
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

    def __str__(self) -> str:
        return self.name


class Person:
    def __init__(
        self, name, temperature, super_market=None, id_list=people_ids
    ) -> None:
        self.id = gen_id(1000, 9999, id_list)
        self.name = name
        self.temperature = float(temperature)
        self.super_market = super_market

        object_data["People"][0].append(self)

        self.start_time = None
        self.end_time = None
        self.state = "out_market"

    def time_elapsed(self):
        return time.time() - self.start_time

    def enter_market(self, super_market):
        self.super_market = super_market
        if self.super_market.temperature_check(self.temperature):
            print("Welcome")
            self.super_market.add_person(self)
            self.start_time = time.time()
            self.state = "in market"
        else:
            print("Sorry Not Allowed!")

    def generate_report(self):
        report = {
            "Person ID": self.id,
            "Supermarket": self.super_market,
            "Temperature": self.temperature,
        }
        return report


# class Menu:
#     def __init__(self) -> None:
#         pass
#     def stateful_menu(self, state):
#         menu_array = global_states.get(state, "invalid state")
#         for index, item in enumerate(menu_array):
#             print(f"{index+1}. " f"{item}")
# menu = Menu()
# menu.stateful_menu("global")

super_market = Supermarket("Walmart", 99.0, object_data["Supermarkets"][1])
person1 = Person("James", 97.7, super_market, object_data["People"][1])
person1.enter_market(super_market)
print(person1.state)
print("============")
person2 = Person("William", 100, super_market, object_data["People"][1])
person2.enter_market(super_market)
print(person2.state)

print(object_data)

# 1. 1243 - Jim
# 2. 3242 - no name provided

