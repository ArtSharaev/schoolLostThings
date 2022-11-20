from os import listdir
import datetime as dt


def check_date(path) -> list:
    arr = []
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
    array = []
    full_path = "flask_app/static/" + path
    for filename in listdir(full_path):
        filename = path + "/" + filename
        array.append(filename)
    sorted_arr_0 = list(sorted(array, key=lambda x: x.split("--")[1]))
    sorted_arr = list(sorted(sorted_arr_0, key=lambda x: x.split("--")[0]))
    return sorted_arr
