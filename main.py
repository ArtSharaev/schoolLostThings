import logging
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware


from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(format=u'%(filename)+13s [ LINE:%(lineno)-4s]'
                           u' %(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.DEBUG,
                    filename='logging.log',
                    filemode='w')
dp.middleware.setup(LoggingMiddleware())

from tg.handlers import *


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':
    executor.start_polling(dp)