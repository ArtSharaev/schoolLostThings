help_message = """
Если вы нашли оставленную вещь, и хотите выложить информацию о ней на сайт, введите команду /add.
Перед отправкой фото проверьте, что её еще нет на сайте lost.protonmos.ru
"""
start_message = """
Здравствуйте!\n
Я - бот для размещения информации о найденных оставленных вещах на сайте lost.protonmos.ru
Для того, чтобы начать работу со мной, введите команду /help
"""
ask_building_message = """
Заполните небольшую анкету для того,
чтобы добавить информацию о найденной вещи на сайт.

Выберите здание, где была найдена вещь.
"""
building_error_message = """
Ошибка, попробуйте еще раз.
"""
ask_room_message = """
Теперь введите номер кабинета, в или возле которого была найдена вещь.
"""
ask_photo = """
Самое главное! Отправьте фотограию найденной вещи.
Не забудьте выбрать пункт "сжать изображение" перед отправкой.
"""
room_error_message = """
Ошибка! Номер кабинета должен быть трехзначным.
"""
finish_message = """
Все готово!\n
Информация о потерянной вещи выложена на сервер. Посмотреть её можно тут:\n
lost.protonmos.ru
"""
choose_photo_to_delete = """
Введите путь к фото, которое хотите удалить.
"""
file_not_found = """
Файл не найден.
"""
file_was_deleted = """
Файл был успешно удалён.
"""
escape = """
Заполнение анкеты было отменено.
"""
MESSAGES = {
    "help": help_message,
    "start": start_message,
    "ask_building": ask_building_message,
    "building_error": building_error_message,
    "ask_room": ask_room_message,
    "room_error": room_error_message,
    "finish": finish_message,
    "choose_photo": choose_photo_to_delete,
    "file_not_found": file_not_found,
    "file_was_deleted": file_was_deleted,
    "escape": escape,
    "ask_photo": ask_photo,
}

BUILDINGS_DICT = {
    "Барклая, дом 15, к. 3": "B15-3",
    "Новозаводская, дом 19": "N19",
    "Большая Филевская, дом 15": "BF15",
    "Филевский б-р, дом 13, к. 2": "FB13-2",
    "Филевский б-р, дом 3, к. 2": "FB3-2",
    "1497": "B15-3",
    "737": "N19",
    "72": "BF15",
    "1114-13": "FB13-2",
    "1114-3": "FB3-2"
}
