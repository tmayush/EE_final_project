# datetime is used for printing the bill
import datetime

# Importing Helper Functions
from supermarket.helper_functions.table import create_table, print_table
from supermarket.helper_functions import input_validation
from supermarket.helper_functions import callback_functions
from supermarket.helper_functions import random_functions

# Importing Functional Logic (Involves entites and report creation)
from supermarket.functional_logic.entities import Supermarket
from supermarket.functional_logic.entities import Person
from supermarket.logging import create_report

# Importing products functions
from supermarket.products import products

# Under Development - Have to work on the choose supermarket function
class GlobalFunctions:
    def __init__(self, my_admin) -> None:
        self.my_admin = my_admin
        self.my_menu = None

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
                    user_input = input_validation.handle_input(
                        question_data[0], question_data[1], "Error: Not a valid number"
                    )
                    results.append(user_input)
                    break
                else:
                    print("Error Value: 2012")
                    break

        Supermarket(results[0], results[1], self.my_menu, id_list)
        # ------------Logging------------
        create_report.create_report("log", self.my_menu)
        # -----------/Logging------------
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
                    user_input = input_validation.handle_input(
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
        Person(results[0], results[1], results[2], self.my_menu, id_list)
        # ------------Logging------------
        create_report.create_report("log", self.my_menu)
        # -----------/Logging------------
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
                user_input = input_validation.handle_input(
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
                user_input = input_validation.handle_input(
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

    def back_functions(self):
        back_statements = {
            "in_market": "person",
            "person": "global",
        }

        self.my_menu.state = back_statements[self.my_menu.state]

    def generate_report(self):
        # file_location = "./supermarket/logging/"
        # file_name = "logging.json"
        create_report.create_report("user_report", self.my_menu)
        # ------------Logging------------
        create_report.create_report("log", self.my_menu)
        # -----------/Logging------------

        return True

    def products(self):
        products.product_selection(self.my_admin.selected_person.bag)
        # ------------Logging------------
        create_report.create_report("log", self.my_menu)
        # -----------/Logging------------

    def checkout(self):
        bag, bill_id, total_amount, supermarket_name, supermarket_city = (
            self.my_admin.selected_person.bag.copy(),
            random_functions.gen_id(1000, 9999, []),
            0,
            self.my_admin.selected_person.super_market.name,
            self.my_admin.selected_person.super_market.city,
        )
        raw_date_info = datetime.datetime.now()
        date_info = {
            "day": raw_date_info.strftime("%d"),
            "month": raw_date_info.strftime("%m"),
            "year": raw_date_info.strftime("%y"),
            "weekday": raw_date_info.strftime("%A"),
            "longtime": raw_date_info.strftime("%X"),
        }
        date_print = f"{date_info['day']}/{date_info['month']}/{date_info['year']}"
        weekday_print = date_info["weekday"]
        time_print = date_info["longtime"]
        while True:
            response = input(
                "There's a 10% discount on your bill, would you like to apply it to your amount? (YES/NO) "
            ).upper()
            if response == "YES" or response == "NO":
                break
            print("Invalid Response")

        # --------------BILL PRINTING--------------
        print(f"\n\t\t\tWelcome to {supermarket_name}")
        print(f"\n\t\t\t  {supermarket_city}")
        print(f"\n\t\t\tBILL ID: {bill_id}\n")
        print(f"DATE: {date_print} | {weekday_print}\t\tTIME: {time_print}\n")
        for index, item in enumerate(bag):
            if index == 0:
                continue
            total_amount += int(item[1]) * int(item[2])
        bag.append(["TOTAL", "", f"{total_amount}"])
        product_bill = create_table(bag, 2)
        print_table(product_bill)
        print("\n")

        if response == "YES":
            total_amount = total_amount - round(0.1 * total_amount)
            print(f"Your new total amount is {total_amount}")

        while True:
            respose = input(f"Press enter to pay {total_amount}/- ")
            if respose == "":
                break
            print('Please press "enter" to pay')
        print("AMOUNT PAYED!")
        print("Thank you for visiting us! Please visit again")
        print("\n")
        # -------------/BILL PRINTING--------------
        # ------------Logging------------
        create_report.create_report("log", self.my_menu)
        # -----------/Logging------------

    def pre_tests(self, state):
        def pre_person():
            return [[self.my_admin.selected_person.name.upper()]]

        pre_content = {"global": None, "person": pre_person, "in_market": pre_person}
        if pre_content[state]:
            final_str = ""
            for arr in pre_content[state]():
                for item in arr:
                    final_str += item
                final_str += "\n"
            return final_str
        else:
            return False
