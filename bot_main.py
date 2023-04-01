import logging
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from logging_lib.submitsLogger import SubmitLogger

with open("tg/BOTTOKEN.txt", "r") as f:
    TOKEN = f.readlines()[0].strip()

# for pythonanywhere
# proxy_url = 'http://proxy.server:3128'
proxy_url = ''
bot = Bot(token=TOKEN, proxy=proxy_url)
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(format=u'%(filename)+13s [ LINE:%(lineno)-4s]'
                           u' %(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.DEBUG,
                    filename='logging_lib/bot-logging.log',
                    filemode='w')
dp.middleware.setup(LoggingMiddleware())
submit_logger = SubmitLogger()

from tg.handlers import *


async def shutdown(dispatcher: Dispatcher) -> None:
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':
    executor.start_polling(dp)
