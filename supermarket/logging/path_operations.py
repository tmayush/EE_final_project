import os


def split_path(file_path):
    splitted = file_path.split("/")
    splitted = list(map(lambda x: x + "/", splitted))
    return splitted


def create_path(relative_path):
    """This allows us to create a path from the root directory
    Depends on the split_path function"""
    relative_path_array = split_path(relative_path)
    final_str = ""
    for folder in relative_path_array:
        final_str += folder
        if not os.path.exists(final_str):
            os.mkdir(final_str)


def get_parent_directory(file_path):
    path = file_path.split("/")
    # Edge case if the last "/" isn't present
    if path[-1] == "":
        path.pop()
    # Pops off the child directory
    child = path.pop()
    # Adds the forward slash at the end as the list only contains directory names
    path = "/".join(path) + "/"
    return [path, child]
