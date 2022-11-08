help_message = """
🛈 Если вы нашли оставленную вещь,
отправьте сюда её фотографию,
и заполните небольшую анкету.
"""
start_message = """
Здравствуйте!
Я - бот для размещения информации о найденных оставленных вещах.
Для того, чтобы начать работу со мной,
ввеждите команду /help
"""
ask_building_message = """
Выберите здание, в котором была найдена вещь.
"""
building_error_message = """
Ошибка, попробуйте еще раз.
"""
ask_room_message = """
Теперь введите номер класса, в или возле которого была найдена вещь.
"""
room_error_message = """
Ошибка! Номер кабинета должен быть трехзначным.
"""
finish_message = """
Все готово! Информация о потерянной вещи выложена на сервер.
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

BUILDINGS_LIST = [
    "Барклая, дом 15, к. 3 (𝟭𝟰𝟵𝟳)",
    "Новозаводская, дом 19 (𝟳𝟯𝟳)",
    "Большая Филевская, дом 15 (𝟳𝟐)",
    "Филевский б-р, дом 13 к. 2 (𝟭𝟭𝟭𝟰)",
    "Филевский б-р, дом 3 к. 2 (𝟭𝟭𝟭𝟰)"
]
