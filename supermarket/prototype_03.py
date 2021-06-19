if __name__ == "__main__":
    import os, sys

    sys.path.append(os.getcwd())

# Importing Helper Functions
from supermarket.helper_functions import input_validation
from supermarket.functional_logic import menu_functions

# Built in Modules - Python 3
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
        # object_data = {"People": [[], []], "Supermarkets": [[], []]}


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
                {"Generate Report": global_functions.generate_report},
                {"Exit": False},
            ]
        }

    def check_changes(self):
        if my_admin.selected_person != None:
            self.global_states["person"] = [
                {"Enter Supermarket": my_admin.selected_person.enter_market},
                {"Exit Supermarket": None},
                {"back": global_functions.back_functions},
            ]
            self.global_states["in_market"] = [
                {"Choose Products": None},
                {"Look Inside Bag": my_admin.selected_person.check_bag},
                {"Check Time Elapsed": my_admin.selected_person.time_elapsed},
                {"back": global_functions.back_functions},
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
            menu_array_length = len(menu_array)
            self.pre_post(menu_array)
            user_input = input_validation.handle_input(
                int, "Choose an option: ", "Error: Not a number"
            )
            print()
            if user_input < 1 or user_input > menu_array_length:
                print("Invalid Index\n")
                continue
            user_input = menu_array[user_input - 1]
            callback_function = list(user_input.values())[0]
            if callback_function == global_functions.choose_person:
                callback_function(self)
            elif callback_function:
                callback_function()
            else:
                break
            self.check_changes()


my_admin = Admin()
global_functions = menu_functions.GlobalFunctions(my_admin)
menu = Menu(my_admin)
global_functions.my_menu = menu

