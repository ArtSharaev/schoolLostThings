import os
from os import listdir
import datetime as dt


def get_outdated_files(building) -> list:
    """Проверка фотографий на истечение срока давности в 1 месяц"""
    arr = []
    if os.path.exists(f"flask_app/static/photos/{building}"):
        for filename in listdir(f"flask_app/static/photos/{building}"):
            date_string = filename.split("--")[0]
            day, month, year = date_string.split("-")
            file_date = dt.date(int(year), int(month), int(day))
            curr_date = dt.datetime.now().date()
            delta = curr_date - file_date
            if delta.days > 30:
                fp = f"flask_app/static/photos/{building}" + "/" + filename
                arr.append(fp)
    return arr


def delete_outdated_files(building) -> None:
    """Удаляем фотографии с истекшим скором давности"""
    for file in get_outdated_files(building):
        os.remove(file)


def generate_unique_filename(date, room_number) -> str:
    """Делаем уникальное имя для файла картинки"""
    k = 0
    new_filename = f"{date}--{room_number}--({k}).jpg"
    while os.path.exists(new_filename):
        k += 1
        new_filename = f"{date}--{room_number}--({k}).jpg"
    return new_filename


def save_photo(building, filename) -> None:
    """Превращаем буферное сохранение в нормальное"""
    os.replace("flask_app/static/photos/base_name.jpg",
               f"flask_app/static/photos/{building}/base_name.jpg")
    os.rename(f"flask_app/static/photos/{building}/base_name.jpg",
              f"flask_app/static/photos/{building}/{filename}")


def get_files(path) -> list:
    """Получение списка фотографий для рендеринга на странице"""
    array = []
    full_path = "flask_app/static/" + path
    if os.path.exists(full_path):

        for filename in listdir(full_path):
            if filename == "base_name.jpg":
                continue
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


def get_formatted_now_date() -> str:
    """Приводим текущую дату к формату ДД-ММ-ГГГГ"""
    now_date = str(dt.datetime.now().date())[::-1]
    date = []
    for part in now_date.split("-"):
        date.append(part[::-1])
    return "-".join(date)