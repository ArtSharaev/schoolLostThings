from aiogram import types
from aiogram.types import ContentType
from tg.utils import States
from tg.messages import MESSAGES, BUILDINGS_DICT
from tg.keyboards import *

import os.path
import os
import datetime as dt
from lib.funks import check_date, update_users_json

from bot_main import submit_logger
from bot_main import dp, bot


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(MESSAGES["start"], reply=False)


@dp.message_handler(commands=['help'])
async def process_help_command(msg: types.Message):
    await bot.send_message(msg.from_user.id, MESSAGES["help"])


@dp.message_handler(content_types=ContentType.PHOTO)
async def process_get_photo_command(msg: types.Message):
    await msg.photo[-1].download("flask_app/static/photos/base_name.jpg")
    state = dp.current_state(user=msg.from_user.id)
    await bot.send_message(msg.from_user.id, MESSAGES["ask_building"],
                           reply_markup=choose_building_markup)
    await state.set_state(States.all()[0])


@dp.message_handler(state=States.STATE1_GET_BUILDING)
async def get_building(msg: types.Message):
    state = dp.current_state(user=msg.from_user.id)
    if msg.text not in BUILDINGS_DICT.keys():
        await bot.send_message(msg.from_user.id, MESSAGES["building_error"],
                               reply_markup=choose_building_markup)
        await state.set_state(States.all()[0])
    else:
        await state.update_data(building=BUILDINGS_DICT[msg.text])
        await bot.send_message(msg.from_user.id, MESSAGES["ask_room"])
        await state.set_state(States.all()[1])


@dp.message_handler(state=States.STATE2_GET_ROOM)
async def get_room(msg: types.Message):
    state = dp.current_state(user=msg.from_user.id)
    try:
        number = int(msg.text)
    except ValueError:
        await bot.send_message(msg.from_user.id, MESSAGES["room_error"])
        await state.set_state(States.all()[1])
    else:
        if number > 999 or number < 100:
            await bot.send_message(msg.from_user.id, MESSAGES["room_error"])
            await state.set_state(States.all()[1])
        else:
            update_users_json(str(msg.from_user.id),
                              str(msg.from_user.full_name))
            state_data = await state.get_data()
            building = state_data["building"]
            prev_date = str(dt.datetime.now().date())[::-1]
            date = []
            for part in prev_date.split("-"):
                date.append(part[::-1])
            date = "-".join(date)
            for filename in check_date(f"flask_app/static/photos/{building}"):
                os.remove(filename)
            k = 0
            new_filename = f"flask_app/static/photos/{building}/{date}--{number}--({k}).jpg"
            while os.path.exists(new_filename):
                k += 1
                new_filename = f"flask_app/static/photos/{building}/{date}--{number}--({k}).jpg"
            os.replace("flask_app/static/photos/base_name.jpg",
                       f"flask_app/static/photos/{building}/base_name.jpg")
            os.rename(f"flask_app/static/photos/{building}/base_name.jpg",
                      new_filename)
            submit_logger.update(msg, str(dt.datetime.now()), number, f"{building}/{date}--{number}--({k}).jpg")
            await bot.send_message(msg.from_user.id, MESSAGES["finish"])
            await state.finish()
