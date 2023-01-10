help_message = """
🛈 Если вы нашли оставленную вещь,
отправьте сюда её фотографию,
и заполните небольшую анкету.
Перед отправкой фото проверьте, 
что её еще нет на сайте https://artsharaev.pythonanywhere.com
"""
start_message = """
Здравствуйте!
Я - бот для размещения информации о найденных оставленных вещах.
Для того, чтобы начать работу со мной, введите команду /help
"""
ask_building_message = """
Выберите здание, в котором была найдена вещь.
"""
building_error_message = """
Ошибка, попробуйте еще раз.
"""
ask_room_message = """
Теперь введите номер кабинета, в или возле которого была найдена вещь.
"""
room_error_message = """
Ошибка! Номер кабинета должен быть трехзначным.
"""
finish_message = """
Все готово!
Информация о потерянной вещи выложена на сервер.
Посмотреть её можно тут 👇
https://artsharaev.pythonanywhere.com
"""

MESSAGES = {
    "help": help_message,
    "start": start_message,
    "ask_building": ask_building_message,
    "building_error": building_error_message,
    "ask_room": ask_room_message,
    "room_error": room_error_message,
    "finish": finish_message,
}

BUILDINGS_DICT = {
    "Барклая, дом 15, к. 3 (𝟭𝟰𝟵𝟳)": "B15-3",
    "Новозаводская, дом 19 (𝟳𝟯𝟳)": "N19",
    "Большая Филевская, дом 15 (𝟳𝟐)": "BF15",
    "Филевский б-р, дом 13 к. 2 (𝟭𝟭𝟭𝟰)": "FB13-2",
    "Филевский б-р, дом 3 к. 2 (𝟭𝟭𝟭𝟰)": "FB3-2",
}
