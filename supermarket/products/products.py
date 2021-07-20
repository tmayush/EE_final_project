from supermarket.helper_functions import table
import json

metadata_file_location = "./supermarket/file_metadata.json"
products = None
with open(metadata_file_location, "r") as metadata_file:
    metadata = json.load(metadata_file)
    products_info = metadata["products_info"]
    with open(
        f"{products_info['file_location']}/{products_info['file_name']}"
    ) as product_file:
        products = json.load(product_file)


def product_selection(person_bag):
    person_bag.append(["ITEMS", "PRICE", "QUANTITY"])
    while True:
        for index, category in enumerate(products.keys()):
            print(f"{index+1}. {category}")

        choice = int(input("Please choose a category: ")) - 1
        print("")

        sub_categorys = list(products.values())[choice]
        for index, sub_category in enumerate(sub_categorys.keys()):
            print(f"{index+1}. {sub_category}")

        choice = int(input("Please choose a sub-category: ")) - 1
        print("")

        items = list(sub_categorys.values())[choice]
        items_arr = [["ITEMS", "PRICE", "ID"]]
        for item_name, item_details in items.items():
            temp_arr = [item_name, f'{item_details["Price"]}', f'{item_details["Id"]}']
            items_arr.append(temp_arr)

        table.print_table(table.create_table(items_arr, 4))

        product_id_input = input(
            "\nPlease enter the ID of the product that you want to add to you bag: "
        )
        quantity = input("What is the quantity of the item that you want to add: ")

        for item_arr in items_arr:
            if product_id_input == item_arr[2]:
                person_bag.append([item_arr[0], item_arr[1], quantity])
                break
        print("\nHere's your current bag\n")
        table.print_table(table.create_table(person_bag, 4))
        continue_shopping = input(
            "\nDo you want to continue shopping? (Yes/No): "
        ).upper()
        if continue_shopping == "YES":
            print("")
            continue
        else:
            break

