import random
import linecache


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
        user["first_name"] = linecache.getline(
            "./male-first-names.txt", random_number(1219)
        ).strip()
    else:
        user["first_name"] = None
    rand = random_number(2)
    if rand == 1:
        user["separator"] = separator()
    else:
        user["separator"] = None
    user["last_name"] = linecache.getline(
        "./last-names.txt", random_number(88799)
    ).strip()
    user["date"] = random_date()
    return user


def create_user_female():
    user = {}
    rand = random_number(2)
    if rand == 1:
        user["first_name"] = linecache.getline(
            "./female-first-names.txt", random_number(1219)
        ).strip()
    else:
        user["first_name"] = None
    rand = random_number(2)
    if rand == 1:
        user["separator"] = separator()
    else:
        user["separator"] = None
    user["last_name"] = linecache.getline(
        "./last-names.txt", random_number(88799)
    ).strip()
    user["date"] = random_date()
    return user


def create_user():
    user = {}
    rand = random_number(3)
    if rand == 1:
        user["first_name"] = linecache.getline(
            "./male-first-names.txt", random_number(1219)
        ).strip()
    elif rand == 2:
        user["first_name"] = linecache.getline(
            "./female-first-names.txt", random_number(4275)
        ).strip()
    else:
        user["first_name"] = None
    rand = random_number(2)
    if rand == 1:
        user["separator"] = separator()
    else:
        user["separator"] = None
    user["last_name"] = linecache.getline(
        "./last-names.txt", random_number(88799)
    ).strip()
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
