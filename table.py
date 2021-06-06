# ------------------DO NOT TOUCH THESE FUNCTIONS-------------
def calculate_max_width(my_list):
    number_of_words = len(my_list[0])
    max_width_list = []
    for word_index in range(number_of_words):
        largest = 0
        for line_index in range(len(my_list)):
            word = my_list[line_index][word_index]
            word_length = len(word)
            if word_length > largest:
                largest = word_length
        max_width_list.append(largest)
    return max_width_list


def distributeSpace(string, max_width=0, space_before=0, space_after=0):
    string_length = len(string)
    if space_before == 0 and space_after == 0:
        space_ba = max_width - string_length
        space_before = space_ba // 2
        space_after = space_ba - space_before
    str_before = " " * space_before
    str_after = " " * space_after
    return f"{str_before}{string}{str_after}"


# ------------------/DO NOT TOUCH THESE FUNCTIONS-------------

# Use this (below)
def create_table(my_list, width_factor, absolute_width=False):
    max_width_list = calculate_max_width(my_list)
    number_of_words = len(my_list[0])
    for word_index in range(number_of_words):
        max_width = max_width_list[word_index] + width_factor
        if absolute_width:
            if width_factor < max(max_width_list):
                return False
            max_width = width_factor
        for line_index in range(len(my_list)):
            old_word = my_list[line_index][word_index]
            new_word = distributeSpace(old_word, max_width=max_width)
            my_list[line_index][word_index] = new_word
    return my_list


hello = [
    ["Cofeee", "24", "1"],
    ["Hamburger", "2454", "2"],
    ["Pancakes", "44", "1"],
]

new_list = create_table(hello, 4)
if new_list:
    for line in new_list:
        final_line = ""
        for word in line:
            final_line += f"|{word}"
        final_line += "|"
        print(final_line)
else:
    print("Table Creation Failed")

