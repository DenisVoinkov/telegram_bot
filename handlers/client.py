from aiogram import Dispatcher, types
from create_bot import dp, bot
from keyboards import kb_client
from data_base import sqlite_db


# @dp.message_handler(commands=['start', 'help'])
async def command_star(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Bon appetit, MEOW (^=◕ᴥ◕=^)', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Communication with the bot takes place through private messages, please write to him, MEOW (ฅ\'ω\'ฅ):\nhttps://t.me/Pizza_SenseiBot')

# @dp.message_handler(commands=['Working_hours'])
async def pizza_working_command(message: types.Message):
     await bot.send_message(message.from_user.id, '9:00 a.m. to 5:00 p.m., Monday to Friday')


# @dp.message_handler(commands=['Location'])
async def pizza_location_command(message: types.Message):
     await bot.send_message(message.from_user.id, '88 North Brickell Street Pittsford, NY 14534')


async def pizza_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_star, commands=['start', 'help'])
    dp.register_message_handler(pizza_working_command, commands=['Working_hours'])
    dp.register_message_handler(pizza_location_command, commands=['Location'])
    dp.register_message_handler(pizza_menu_command, commands='Menu')
