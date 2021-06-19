if __name__ == "__main__":
    import os, sys

    sys.path.append(os.getcwd())
    # os.chdir(os.getcwd() + "\\supermarket")
    # print(os.getcwd())

# from supermarket import prototype_03
# from supermarket.functional_logic import entities
# from supermarket.prototype_03 import menu
from supermarket.logging import json_operations
from supermarket.helper_functions import error_handling
from supermarket.logging import path_operations


def log_me(menu, metadata_file):
    metadata = json_operations.read_json_object(metadata_file)
    if metadata:
        # Once it gets the metadata, we will extract the metadata for the log
        metadata = metadata.get("logger_info", "Invalid Key")
        path_operations.create_path(metadata["file_location"])
    # Raises an Exception in case it fails to read the metadata
    else:
        raise Exception(
            error_handling.decorate_error(
                f"Error: File {metadata_file} not found! Error from {__file__}\n"
            )
        )
    final_stuff = dict()
    for entity, keys in menu.my_admin.object_data.items():
        final_stuff[entity] = []
        for created_entity in keys[0]:
            final_stuff[entity].append(created_entity.generate_report())
    json_operations.write_json_object(
        final_stuff, metadata["file_location"] + metadata["file_name"]
    )


def user_report(menu, metadata_file):
    # Reads the metadata_file which contains all the metadata about the project
    metadata = json_operations.read_json_object(metadata_file)
    if metadata:
        # Once it gets the metadata, we will extract the metadata for the report
        metadata = metadata.get("report_info", "Invalid Key")
        path_operations.create_path(metadata["file_location"])
    # Raises an Exception in case it fails to read the metadata
    else:
        raise Exception(
            error_handling.decorate_error(
                f"Error: File {metadata_file} not found! Error from {__file__}\n"
            )
        )
    final_stuff = dict()
    for entity, keys in menu.my_admin.object_data.items():
        final_stuff[entity] = []
        for created_entity in keys[0]:
            final_stuff[entity].append(created_entity.generate_report())

    json_operations.write_json_object(
        final_stuff, metadata["file_location"] + metadata["file_name"]
    )


def create_report(report_type, menu):
    metadata_file = "./supermarket/file_metadata.json"
    report_types = {
        "log": log_me,
        "user_report": user_report,
    }
    function_call = report_types.get(report_type, False)
    if function_call:
        function_call(menu, metadata_file)
