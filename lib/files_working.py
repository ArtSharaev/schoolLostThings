import os
from os import listdir
import datetime as dt


def get_outdated_files(path_to_dir) -> list:
    """Проверка фотографий на истечение срока давности в 1 месяц"""
    arr = []
    if os.path.exists(path_to_dir):
        for filename in listdir(path_to_dir):
            date_string = filename.split("--")[0]
            day, month, year = date_string.split("-")
            file_date = dt.date(int(year), int(month), int(day))
            curr_date = dt.datetime.now().date()
            delta = curr_date - file_date
            if delta.days > 30:
                fp = path_to_dir + "/" + filename
                arr.append(fp)
    return arr


def del_outdated_files(path_to_dir) -> None:
    """Удаляем фотографии с истекшим скором давности"""
    for file in get_outdated_files(path_to_dir):
        os.remove(file)


def generate_unique_filename(path_to_dir, date, room_number) -> str:
    """Делаем уникальное имя для файла картинки"""
    k = 0
    new_filename = f"{path_to_dir}/{date}--{room_number}--({k}).jpg"
    while os.path.exists(new_filename):
        k += 1
        new_filename = f"{path_to_dir}/{date}--{room_number}--({k}).jpg"
    return new_filename


def save_photo(path_to_dir, filename) -> None:
    """Превращаем буферное сохранение в нормальное"""
    os.replace("flask_app/static/photos/base_name.jpg",
               f"{path_to_dir}/base_name.jpg")
    os.rename(f"{path_to_dir}/base_name.jpg",
              filename)
