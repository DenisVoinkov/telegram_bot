from aiogram import Dispatcher, types
import string, json
from create_bot import dp

# @dp.message_handler()
async def filter(message: types.Message):  # фильтер матов
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('/Users/unknown1/Documents/Python/telegram_bot/cenz.json')))):
            await message.reply('Don\'t be so rude, don\'t upset the cat, MEOW ฅ(≚ᄌ≚)')
            await message.delete()


def register_handlers_general(dp: Dispatcher):
    dp.register_message_handler(filter)
