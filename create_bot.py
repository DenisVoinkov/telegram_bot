from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storge = MemoryStorage()


TOKEN = '5476648736:AAFfI5nIW3rt-7sAOiRDEBYhcIGPIuvxBak'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storge)
