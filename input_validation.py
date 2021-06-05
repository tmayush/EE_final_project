def check_input(user_input, data_type):
    if type(user_input) is data_type:
        return True
    else:
        return False


def change_input_type(user_input, data_type):
    if data_type is str:
        try:
            return str(user_input)
        except:
            return False
    elif data_type is int:
        try:
            return int(user_input)
        except:
            return False
    elif data_type is float:
        try:
            return float(user_input)
        except:
            return False
    elif data_type is bool:
        return bool(user_input)


def handle_input(input_data_type, custom_query=None, custom_error=None):
    if (
        input_data_type is str
        and custom_query is not None
        and custom_error is not None
        and check_input(custom_query, str)
        and check_input(custom_error, str)
    ):
        user_input = input(custom_query)
        return user_input
    elif (
        custom_query is not None
        and custom_error is not None
        and check_input(custom_query, str)
        and check_input(custom_error, str)
    ):
        returned_output = False
        while returned_output is False:
            user_input = input(custom_query)
            returned_output = change_input_type(user_input, input_data_type)
            if returned_output is False:
                print(f"{custom_error}\n")
    else:
        if input_data_type is int:
            placeholder_datatype = "Number"
        elif input_data_type is str:
            placeholder_datatype = "String"
        elif input_data_type is float:
            placeholder_datatype = "Float Value"

        returned_output = False
        while returned_output is False:
            user_input = input(f"Please Enter a {placeholder_datatype}: ")
            returned_output = change_input_type(user_input, input_data_type)
            if returned_output is False:
                print(f"Error: Input was not a {placeholder_datatype}\n")
    return returned_output
