import json


def write_json_object(python_object, file_name):
    with open(file_name, "w") as file:
        json.dump(python_object, file)


def read_json_object(file_name):
    python_object = False
    try:
        with open(file_name, "r") as file:
            python_object = json.load(file)
    except:
        print("Error: File Not Found!")
        return False
    return python_object

