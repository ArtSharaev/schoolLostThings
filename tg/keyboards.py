from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton

choose_building_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                             one_time_keyboard=True)
btn1 = KeyboardButton("Барклая, дом 15, к. 3")
btn2 = KeyboardButton("Новозаводская, дом 19")
choose_building_markup.row(btn1, btn2)
btn3 = KeyboardButton("Большая Филевская, дом 15")
choose_building_markup.row(btn3)
btn4 = KeyboardButton("Филевский б-р, дом 13, к. 2")
btn5 = KeyboardButton("Филевский б-р, дом 3, к. 2")
choose_building_markup.row(btn4, btn5)
btn6 = KeyboardButton("Отмена")
choose_building_markup.row(btn6)

escape_markup = ReplyKeyboardMarkup(resize_keyboard=True)
btn = KeyboardButton("Отмена")
escape_markup.row(btn)

add_markup = ReplyKeyboardMarkup(resize_keyboard=True)
btn_add = KeyboardButton(text="/add")
add_markup.row(btn_add)

empty_markup = ReplyKeyboardRemove()
