from aiogram import types
from aiogram.types import ContentType, InputFile
from tg.utils import UserStates, AdminStates
from tg.messages import MESSAGES, BUILDINGS_DICT
from tg.keyboards import *
import datetime as dt
from tools.tools import delete_outdated_files, \
    generate_unique_filename, get_formatted_now_date, is_admin
from bot_main import submit_logger
from bot_main import dp, bot
import os


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(MESSAGES["start"], reply=False,
                        reply_markup=add_markup)


@dp.message_handler(commands=['help'])
async def process_help_command(msg: types.Message):
    await bot.send_message(msg.from_user.id, MESSAGES["help"],
                           reply_markup=add_markup)


@dp.message_handler(commands=['add'])
async def process_add_command(msg: types.Message):
    state = dp.current_state(user=msg.from_user.id)
    await bot.send_message(msg.from_user.id, MESSAGES["ask_building"],
                           reply_markup=choose_building_markup)
    await state.set_state(UserStates.all()[0])


@dp.message_handler(state=UserStates.STATE1_GET_BUILDING)
async def get_building(msg: types.Message):
    state = dp.current_state(user=msg.from_user.id)
    if msg.text == "Отмена":
        await bot.send_message(msg.from_user.id, MESSAGES["escape"],
                               reply_markup=add_markup)
        await state.finish()
    elif msg.text not in BUILDINGS_DICT.keys():
        await bot.send_message(msg.from_user.id, MESSAGES["building_error"],
                               reply_markup=choose_building_markup)
        await state.set_state(UserStates.all()[0])
    else:
        await state.update_data(building=BUILDINGS_DICT[msg.text])
        await bot.send_message(msg.from_user.id, MESSAGES["ask_room"],
                               reply_markup=escape_markup)
        await state.set_state(UserStates.all()[1])


@dp.message_handler(state=UserStates.STATE2_GET_ROOM)
async def get_room(msg: types.Message):
    state = dp.current_state(user=msg.from_user.id)
    if msg.text == "Отмена":
        await bot.send_message(msg.from_user.id, MESSAGES["escape"],
                               reply_markup=add_markup)
        await state.finish()
    else:
        try:
            room_number = msg.text
            # if not 100 <= room_number <= 999:
            #     raise ValueError
        except ValueError:
            await bot.send_message(msg.from_user.id, MESSAGES["room_error"],
                                   reply_markup=escape_markup)
            await state.set_state(UserStates.all()[1])
        else:
            await state.update_data(room=room_number)
            await bot.send_message(msg.from_user.id, MESSAGES["ask_photo"],
                                   reply_markup=empty_markup)
            await state.set_state(UserStates.all()[2])


@dp.message_handler(state=UserStates.STATE3_GET_PHOTO,
                    content_types=ContentType.PHOTO)
async def get_photo(msg: types.Message):
    state = dp.current_state(user=msg.from_user.id)
    state_data = await state.get_data()
    building = state_data["building"]
    room = state_data["room"]
    date = get_formatted_now_date()
    delete_outdated_files(building)
    filename = generate_unique_filename(building, date, room)
    await msg.photo[-1].download(
        f"flask_app/static/photos/{building}/{filename}")
    submit_logger.update(msg, str(dt.datetime.now()), room,
                         f"{building}/{filename}")
    await bot.send_message(msg.from_user.id, MESSAGES["finish"],
                           reply_markup=add_markup)
    await state.finish()


@dp.message_handler(commands=['get'])
async def process_get_command(msg: types.Message):
    if is_admin(msg.from_user.id):
        state = dp.current_state(user=msg.from_user.id)
        await bot.send_message(msg.from_user.id, MESSAGES["ask_building"],
                               reply_markup=choose_building_markup)
        await state.set_state(AdminStates.all()[0])


@dp.message_handler(state=AdminStates.ADMIN_GET_BUILDING)
async def get_building_to_delete(msg: types.Message):
    state = dp.current_state(user=msg.from_user.id)
    if msg.text not in BUILDINGS_DICT.keys():
        await bot.send_message(msg.from_user.id, MESSAGES["building_error"],
                               reply_markup=add_markup)
    else:
        building = BUILDINGS_DICT[msg.text]
        for file in os.listdir(f"flask_app/static/photos/{building}"):
            if file != ".gitignore":
                with open(f"flask_app/static/photos/{building}/{file}",
                          "rb") as photo:
                    await bot.send_photo(msg.from_user.id, photo,
                                         f"{building}/{file}",
                                         reply_markup=add_markup)
    await state.finish()


@dp.message_handler(commands=['del'])
async def process_del_command(msg: types.Message):
    if is_admin(msg.from_user.id):
        state = dp.current_state(user=msg.from_user.id)
        await bot.send_message(msg.from_user.id, MESSAGES["choose_photo"],
                               reply_markup=add_markup)
        await state.set_state(AdminStates.all()[1])


@dp.message_handler(state=AdminStates.ADMIN_GET_PHOTO_TO_DELETE)
async def get_photo_to_delete(msg: types.Message):
    state = dp.current_state(user=msg.from_user.id)
    file = msg.text
    if not os.path.exists(f"flask_app/static/photos/{file}"):
        await bot.send_message(msg.from_user.id, MESSAGES["file_not_found"],
                               reply_markup=add_markup)
    else:
        os.remove(f"flask_app/static/photos/{file}")
        await bot.send_message(msg.from_user.id, MESSAGES["file_was_deleted"],
                               reply_markup=add_markup)
    await state.finish()
