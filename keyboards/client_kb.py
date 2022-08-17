from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/Working_hours')
b2 = KeyboardButton('/Location')
b3 = KeyboardButton('/Menu')
b4 = KeyboardButton('/Share number', request_contact=True)
b5 = KeyboardButton('/Send where i\'am', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b1).add(b2).add(b3).row(b4, b5)
