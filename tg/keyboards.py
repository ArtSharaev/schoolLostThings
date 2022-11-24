from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton


choose_building_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                             one_time_keyboard=True)
btn1 = KeyboardButton("Барклая, дом 15, к. 3 (𝟭𝟰𝟵𝟳)")
btn2 = KeyboardButton("Новозаводская, дом 19 (𝟳𝟯𝟳)")
choose_building_markup.row(btn1, btn2)
btn3 = KeyboardButton("Большая Филевская, дом 15 (𝟳𝟐)")
choose_building_markup.row(btn3)
btn4 = KeyboardButton("Филевский б-р, дом 13 к. 2 (𝟭𝟭𝟭𝟰)")
btn5 = KeyboardButton("Филевский б-р, дом 3 к. 2 (𝟭𝟭𝟭𝟰)")
choose_building_markup.row(btn4, btn5)