import random
from datetime import date

male_first_names = open(
    "./male-first-names.txt", mode="r", encoding="utf-8"
).readlines()
female_first_names = open(
    "./female-first-names.txt", mode="r", encoding="utf-8"
).readlines()
last_names = open("./last-names.txt", mode="r", encoding="utf-8").readlines()


def random_from(flag=0):
    result = (
        last_names[random_number(len(last_names)) - 1][:-1]
        if flag == 0
        else male_first_names[random_number(len(male_first_names)) - 1][:-1]
        if flag == 1
        else female_first_names[random_number(len(female_first_names)) - 1][:-1]
    )
    return result


def random_number(last):
    return random.randrange(1, last + 1)


def random_date():
    return random.randrange(1, date.today().year)


def separator():
    seps = [".", "_"]
    return seps[random_number(2) - 1]


def create_user(gender="both"):
    user = {}
    if gender == "male":
        rand = random_number(2)
        user["first_name"] = random_from(1) if rand == 1 else None
    elif gender == "female":
        rand = random_number(2)
        user["first_name"] = random_from(2) if rand == 1 else None
    else:
        rand = random_number(3)
        user["first_name"] = (
            random_from(1) if rand == 1 else random_from(2) if rand == 2 else None
        )
    rand = random_number(2)
    user["separator"] = separator() if rand == 1 else None
    user["last_name"] = random_from(0)
    user["date"] = random_date()
    return user


def convert_to_string(user):
    return f"{user['first_name'] if user['first_name'] else ''}{user['separator'] if user['separator'] else ''}{user['last_name']}{user['date']}"


def create_several_user(amount=1, gender="both"):
    users = set()
    while len(users) != amount:
        usr = create_user(gender=gender)
        users.add(convert_to_string(usr))
    return list(users)
