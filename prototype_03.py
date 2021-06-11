from random_functions import *
from input_validation import handle_input
from table import create_table
import callback_functions
import time


class Admin:
    def __init__(self) -> None:
        self.selected_person = None
        self.people = []
        self.people_ids = []
        self.supermarkets = []
        self.sp_ids = []
        self.object_data = {
            "People": [self.people, self.people_ids],
            "Supermarkets": [self.supermarkets, self.sp_ids],
        }


class GlobalFunctions:
    def __init__(self, my_admin) -> None:
        self.my_admin = my_admin

    def create_supermarket(self):
        id_list = self.my_admin.object_data["Supermarkets"][1]
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

    def create_person(self):
        id_list = self.my_admin.object_data["People"][1]
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
        chosen_sp = self.choose_supermarket()
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

    def choose_supermarket(self):
        supermarkets, result = self.my_admin.object_data["Supermarkets"][0], []
        if len(supermarkets) == 0:
            print("No Supermarkets created!\n")
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
                    print(f"You chose: {supermarkets[user_input-1]}\n")
                    result.append(True)
                    result.append(supermarkets[user_input - 1])
                    return result
                else:
                    print("Invalid Serial Number\n")

    def choose_person(self, my_menu):
        people, result = self.my_admin.object_data["People"][0], []
        if len(people) == 0:
            print("No people created!\n")
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
                    print(f"You chose: {people[user_input-1]}\n")
                    result.append(True)
                    result.append(people[user_input - 1])
                    self.my_admin.selected_person = result[1]
                    # Updates state
                    my_menu.state = "person"
                    return result
                else:
                    print("Invalid Serial Number\n")

    def pre_tests(self, state):
        def pre_person():
            return [[self.my_admin.selected_person.name.upper()]]

        pre_content = {"global": None, "person": pre_person, "in_market": None}
        if pre_content[state]:
            final_str = ""
            for arr in pre_content[state]():
                for item in arr:
                    final_str += item
                final_str += "\n"
            return final_str
        else:
            return False


class Supermarket:
    def __init__(self, name, max_temperature, id_list) -> None:
        self.name = name
        self.id = gen_id(1, 100, id_list)
        self.max_temperature = float(max_temperature)
        self.people = []

        id_list.append(self.id)
        my_admin.object_data["Supermarkets"][0].append(self)

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

    def __str__(self) -> str:
        return self.name


# Under development - Products interaction
class Person:
    def __init__(self, name, temperature, super_market, id_list) -> None:
        self.id = gen_id(1000, 9999, id_list)
        self.name = name
        self.temperature = float(temperature)
        self.super_market = super_market
        # self.bag = []
        self.bag = [
            ["Cofeee", "24", "1"],
            ["Hamburger", "2454", "2"],
            ["Pancakes", "44", "1"],
        ]

        id_list.append(self.id)
        my_admin.object_data["People"][0].append(self)

        self.menu = menu
        self.start_time = None
        self.end_time = None
        self.state = "out_market"

    def time_elapsed(self):
        calc_time_elapsed = time.time() - self.start_time
        print(f"Time Elapsed - {calc_time_elapsed}\n")
        return calc_time_elapsed

    def enter_market(self):
        # self.super_market = super_market
        if self.super_market.temperature_check(self.temperature):
            print("Welcome\n")
            self.super_market.add_person(self)
            self.start_time = time.time()
            self.state = "in_market"
            self.menu.state = "in_market"
        else:
            print("Sorry Not Allowed!")

    def check_bag(self):
        if len(self.bag) == 0:
            print("No items present\n")
            return None
        else:
            new_list = create_table(self.bag, 4)
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
            "Supermarket": self.super_market,
            "Temperature": self.temperature,
        }
        return report

    def __str__(self) -> str:
        return self.name


# Under development
class Menu:
    def __init__(self, my_admin, state="global") -> None:
        self.state = state
        self.my_admin = my_admin
        self.global_states = {
            "global": [
                {"Create Supermarket": global_functions.create_supermarket},
                {"Create Person": global_functions.create_person},
                {"Choose Supermarket": global_functions.choose_supermarket},
                {"Choose Person": global_functions.choose_person},
                {"Exit": False},
            ]
        }

    def check_changes(self):
        if my_admin.selected_person != None:
            self.global_states["person"] = [
                {"Enter Supermarket": my_admin.selected_person.enter_market},
                {"Exit Supermarket": None},
                {"back": False},
            ]
            self.global_states["in_market"] = [
                {"Choose Products": None},
                {"Look Inside Bag": my_admin.selected_person.check_bag},
                {"Check Time Elapsed": my_admin.selected_person.time_elapsed},
                {"back": False},
            ]

    def pre_post(self, menu_array):
        pre_content = global_functions.pre_tests(self.state)
        if pre_content:
            print(pre_content)
        for index, item in enumerate(menu_array):
            print(f"{index+1}. " f"{list(item.keys())[0]}")

    def stateful_menu(self):
        while True:
            menu_array = self.global_states.get(self.state, "invalid state")
            self.pre_post(menu_array)
            user_input = handle_input(int, "Choose an option: ", "Error: Not a number")
            print()
            user_input = menu_array[user_input - 1]
            callback_function = list(user_input.values())[0]
            if callback_function == global_functions.choose_person:
                callback_function(self)
            elif callback_function:
                callback_function()
            else:
                break
            self.check_changes()


if __name__ == "__main__":
    my_admin = Admin()
    global_functions = GlobalFunctions(my_admin)
    menu = Menu(my_admin)
    menu.stateful_menu()
    print(my_admin.selected_person)
# object_data = {"People": [[], []], "Supermarkets": [[], []]}