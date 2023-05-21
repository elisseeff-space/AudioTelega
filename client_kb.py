from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove

b1 = KeyboardButton('/ru')
b2 = KeyboardButton('/en')
b3 = KeyboardButton('/fr')
b4 = KeyboardButton('Share your PhoneNumber', request_contact=True)
#b5 = KeyboardButton('Send Where I Am', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

#kb_client.add(b1).add(b2).add(b3).row(b4, b5)
kb_client.row(b1, b2, b3).add(b4)
#kb_client.add(b1).add(b2).insert(b3)
#kb_client.row(b1, b2, b3)
