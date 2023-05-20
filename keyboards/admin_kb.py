from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove

# Admin Keyboard Buttons
button_stat = KeyboardButton('/Statistics')
button_delete = KeyboardButton('/Delete')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_stat).add(button_delete)