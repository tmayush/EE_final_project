def range_of_value(value, min, max):
    if type(value) is int or type(value) is float:
        if value >= min and value <= max:
            return True
        return False
    else:
        print("not an integer")
        return None


def string_limit(value, min, max):
    if type(value) is str:
        if len(value) >= min and len(value) <= max:
            return True
        return False
    else:
        print("not a string")
        return None

