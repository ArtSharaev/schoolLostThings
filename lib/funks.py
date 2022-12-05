import os
from os import listdir
import datetime as dt
import json


def check_date(path) -> list:
    """Проверка фотографий на истечение срока давности в 1 месяц"""
    arr = []
    if not os.path.exists(path):
        os.mkdir(path)
    for filename in listdir(path):
        date = filename.split("--")[0]
        month = date.split("-")[1]
        if month != str(dt.datetime.now().month):
            cur_day = int(dt.datetime.now().day)
            day = int(date.split("-")[0])
            if day >= 28 and cur_day >= 28:
                ffp = path + "/" + filename
                arr.append(ffp)
            elif day <= cur_day:
                ffp = path + "/" + filename
                arr.append(ffp)
    return arr


def get_files(path) -> list:
    """Сортировка фотографий по дате"""
    array = []
    full_path = "flask_app/static/" + path
    if os.path.exists(full_path):
        for filename in listdir(full_path):
            filename = path + "/" + filename
            array.append(filename)
        sorted_array = list(reversed(sorted(array,
                                            key=lambda x: int(
                                                x.split("/")[-1].split("--")[
                                                    0].split("-")[0]))))
        sorted_array = list(sorted(sorted_array,
                                   key=lambda x: -int(
                                       x.split("/")[-1].split("--")[0].split("-")[
                                           1])))
        return sorted_array
    return array


def update_users_json(user_id, user_fullname):
    """Добавляем пользователя или обновляем информацию о нем"""
    with open("users_data/users.json", "r") as users:
        data = json.load(users)

    data[user_id] = [user_fullname, str(dt.datetime.now())]

    with open("users_data/users.json", "w") as users:
        json.dump(data, users)
