from random_functions import *
from input_validation import handle_input
import callback_functions
import time

people = []
people_ids = []
supermarkets = []
sp_ids = []
currently_selected = None
object_data = {"People": [people, people_ids], "Supermarkets": [supermarkets, sp_ids]}
# object_data = {"People": [[], []], "Supermarkets": [[], []]}


def create_supermarket(id_list=object_data["Supermarkets"][1]):
    results = []
    questions = [
        [
            str,
            "Please enter the name of the supermarket: ",
            callback_functions.string_limit,
        ],
        [float, "Please enter the temperature limit of the supermarket: ", None],
    ]
    for question_data in questions:
        while True:
            if question_data[0] is str:
                user_input = input(question_data[1])
                if question_data[2](user_input, 1, 20):
                    results.append(user_input)
                    break
            elif question_data[0] is int or question_data[0] is float:
                user_input = handle_input(
                    question_data[0], question_data[1], "Error: Not a valid number"
                )
                results.append(user_input)
                break
            else:
                print("Error Value: 2012")
                break

    super_market = Supermarket(results[0], results[1], id_list)
    return True


def create_person(id_list=object_data["People"][1]):
    results = []
    questions = [
        [
            str,
            "Please enter the name of the person: ",
            callback_functions.string_limit,
        ],
        [float, "Please enter the temperature of the person: ", None],
    ]
    for question_data in questions:
        while True:
            if question_data[0] is str:
                user_input = input(question_data[1])
                if question_data[2](user_input, 1, 30):
                    results.append(user_input)
                    break
            elif question_data[0] is int or question_data[0] is float:
                user_input = handle_input(
                    question_data[0], question_data[1], "Error: Not a valid number"
                )
                results.append(user_input)
                break
            else:
                print("Error Value: 2017")
                break
    print("To create a person, that person must belong to a supermarket")
    chosen_sp = choose_supermarket()
    if chosen_sp[0]:
        results.append(chosen_sp[1])
    else:
        print(
            f"Since there are no supermarkets we couldn't create {results[0]},\n"
            f"please create a supermarket to create {results[0]}"
        )
        return False
    Person(results[0], results[1], results[2], id_list)
    return True


def choose_supermarket():
    supermarkets, result = object_data["Supermarkets"][0], []
    if len(supermarkets) == 0:
        print("No Supermarkets created!")
        result.append(False)
        return result
    else:
        print(
            "Please choose one of the following supermarkets by entering its Serial Number:"
        )
        for index, supermarket in enumerate(supermarkets):
            print(f"{index + 1}. {supermarket}")
        print()
        while True:
            user_input = handle_input(
                int, "Supermarket Serial Number: ", "Error: Not a number"
            )
            if user_input > 0 and user_input < index + 2:
                print(f"You chose: {supermarkets[user_input-1]}")
                result.append(True)
                result.append(supermarkets[user_input - 1])
                return result
            else:
                print("Invalid Serial Number\n")


def choose_person():
    people, result = object_data["People"][0], []
    if len(people) == 0:
        print("No people created!")
        result.append(False)
        return result
    else:
        print(
            "Please choose one of the following people by entering their Serial Number:"
        )
        for index, person in enumerate(people):
            print(f"{index + 1}. {person}")
        print()
        while True:
            user_input = handle_input(
                int, "person Serial Number: ", "Error: Not a number"
            )
            if user_input > 0 and user_input < index + 2:
                print(f"You chose: {people[user_input-1]}")
                result.append(True)
                result.append(people[user_input - 1])
                currently_selected = result[1]
                return result
            else:
                print("Invalid Serial Number\n")


global_states = {
    "global": [
        {"Create Supermarket": create_supermarket},
        {"Create Person": create_person},
        {"Choose Supermarket": choose_supermarket},
        {"Choose Person": choose_person},
        {"Exit": False},
    ],
    "person": [
        {"Choose Products": None},
        {"Enter Supermarket": None},
        {"Exit Supermarket": None},
        {"back": False},
    ],
}


class Supermarket:
    def __init__(self, name, max_temperature, id_list=sp_ids) -> None:
        self.name = name
        self.id = gen_id(1, 100, id_list)
        self.max_temperature = float(max_temperature)
        self.people = []

        id_list.append(self.id)
        object_data["Supermarkets"][0].append(self)

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


# Under development - Products interaction
class Person:
    def __init__(
        self, name, temperature, super_market=None, id_list=people_ids
    ) -> None:
        self.id = gen_id(1000, 9999, id_list)
        self.name = name
        self.temperature = float(temperature)
        self.super_market = super_market
        self.bag = []

        id_list.append(self.id)
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

    def __str__(self) -> str:
        return self.name


# Under development
class Menu:
    def __init__(self) -> None:
        pass

    def stateful_menu(self, state):
        while True:
            menu_array = global_states.get(state, "invalid state")
            for index, item in enumerate(menu_array):
                print(f"{index+1}. " f"{list(item.keys())[0]}")
            user_input = handle_input(int, "Choose an option: ", "Error: Not a number")
            user_input = menu_array[user_input - 1]
            callback_function = list(user_input.values())[0]
            if callback_function:
                callback_function()
            else:
                break


menu = Menu()
menu.stateful_menu("global")

# super_market = Supermarket("Walmart", 99.0, object_data["Supermarkets"][1])
# person1 = Person("James", 97.7, super_market, object_data["People"][1])
# person1.enter_market(super_market)
# print(person1.state)
# print("============")
# person2 = Person("William", 100, super_market, object_data["People"][1])
# person2.enter_market(super_market)
# print(person2.state)

# print(object_data)
# test1 = choose_supermarket()
# test2 = choose_person()
# test1 = create_supermarket()
# test2 = create_person()

# print(test1, test2)

# print(object_data)
# menu.stateful_menu("global")
print(currently_selected)
print(currently_selected.name)
