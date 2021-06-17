import random


def gen_random_int(min, max):
    return round(random.random() * (max - min)) + min


def gen_random_list(min, max, length):
    random_list = []
    for i in range(length):
        random_list.append(gen_random_int(min, max))
    return random_list


def gen_random_aplhabet():
    return chr(gen_random_int(97, 122))


def gen_random_char():
    return chr(gen_random_int(33, 126))


def gen_id(min, max, id_list):
    id = gen_random_int(min, max)
    while id in id_list:
        id = gen_random_int(min, max)
    return id
