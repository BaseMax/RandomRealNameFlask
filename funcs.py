import random
import linecache

male_first_names = open(
    "./male-first-names.txt", mode="r", encoding="utf-8"
).readlines()
female_first_names = open(
    "./female-first-names.txt", mode="r", encoding="utf-8"
).readlines()
last_names = open("./last-names.txt", mode="r", encoding="utf-8").readlines()


def random_number(last):
    return random.randrange(1, last + 1)


def random_date():
    return random.randrange(1, 2023)


def separator():
    seps = [".", "_"]
    return seps[random_number(2) - 1]


def create_user_male():
    user = {}
    rand = random_number(2)
    if rand == 1:
        user["first_name"] = male_first_names[random_number(1219) - 1][:-1]
    else:
        user["first_name"] = None
    rand = random_number(2)
    if rand == 1:
        user["separator"] = separator()
    else:
        user["separator"] = None
    user["last_name"] = last_names[random_number(88799) - 1][:-1]
    user["date"] = random_date()
    return user


def create_user_female():
    user = {}
    rand = random_number(2)
    if rand == 1:
        user["first_name"] = female_first_names[random_number(4275) - 1][:-1]
    else:
        user["first_name"] = None
    rand = random_number(2)
    if rand == 1:
        user["separator"] = separator()
    else:
        user["separator"] = None
    user["last_name"] = last_names[random_number(88799) - 1][:-1]
    user["date"] = random_date()
    return user


def create_user():
    user = {}
    rand = random_number(3)
    if rand == 1:
        user["first_name"] = male_first_names[random_number(1219) - 1][:-1]
    elif rand == 2:
        user["first_name"] = female_first_names[random_number(4275) - 1][:-1]
    else:
        user["first_name"] = None
    rand = random_number(2)
    if rand == 1:
        user["separator"] = separator()
    else:
        user["separator"] = None
    user["last_name"] = last_names[random_number(88799) - 1][:-1]
    user["date"] = random_date()
    return user


def convert_to_string(user):
    return f"{user['first_name'] if user['first_name'] else ''}{user['separator'] if user['separator'] else ''}{user['last_name']}{user['date']}"


def create_several_user(amount):
    users = set()
    while len(users) != amount:
        usr = create_user()
        users.add(convert_to_string(usr))
    return list(users)


def create_several_user_male(amount):
    users = set()
    while len(users) != amount:
        usr = create_user_male()
        users.add(convert_to_string(usr))
    return list(users)


def create_several_user_female(amount):
    users = set()
    while len(users) != amount:
        usr = create_user_female()
        users.add(convert_to_string(usr))
    return list(users)
