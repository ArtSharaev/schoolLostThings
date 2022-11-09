from aiogram import types
from aiogram.types import ContentType
from tg.utils import States
from tg.messages import MESSAGES, BUILDINGS_LIST
from tg.keyboards import *
import os
import os.path

from main import dp, bot


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(MESSAGES["start"], reply=False)


@dp.message_handler(commands=['help'])
async def process_help_command(msg: types.Message):
    await bot.send_message(msg.from_user.id, MESSAGES["help"])


@dp.message_handler(content_types=ContentType.PHOTO)
async def process_get_photo_command(msg: types.Message):
    await msg.photo[-1].download("photos/base_name.jpg")
    state = dp.current_state(user=msg.from_user.id)
    await bot.send_message(msg.from_user.id, MESSAGES["ask_building"],
                           reply_markup=choose_building_markup)
    await state.set_state(States.all()[0])


@dp.message_handler(state=States.STATE1_GET_BUILDING)
async def process_get_building_command(msg: types.Message):
    state = dp.current_state(user=msg.from_user.id)
    if msg.text not in BUILDINGS_LIST:
        await bot.send_message(msg.from_user.id, MESSAGES["building_error"],
                               reply_markup=choose_building_markup)
        await state.set_state(States.all()[0])
    else:
        await state.update_data(building=msg.text)
        await bot.send_message(msg.from_user.id, MESSAGES["ask_room"])
        await state.set_state(States.all()[1])


@dp.message_handler(state=States.STATE2_GET_ROOM)
async def process_get_room_command(msg: types.Message):
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
            state_data = await state.get_data()
            building = state_data["building"]
            k = 0
            new_filename = f"photos/{building}--{number}--({k}).jpg"
            while os.path.exists(new_filename):
                k += 1
                new_filename = f"photos/{building}--{number}--({k}).jpg"
            os.rename("photos/base_name.jpg", new_filename)
            await bot.send_message(msg.from_user.id, MESSAGES["finish"])
            await state.finish()
