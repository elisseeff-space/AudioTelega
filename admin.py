#import pandas as pd
#import datetime as dt
import io

from aiogram import Dispatcher, types
#from aiogram.dispatcher import FSMContext
#from aiogram.dispatcher.filters import Text
#from aiogram.dispatcher.filters.state import State, StatesGroup
#from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import audio_sqlite_db
import admin_kb

from create_bot import bot, dp

idd = None

# Get Moderator Id 
# @dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def moderator_command(message: types.Message):
    global idd
    idd = message.from_user.id
    await bot.send_message(message.from_user.id, 'What do you want Sir?', reply_markup=admin_kb.button_case_admin)
    await message.delete()


# Start Menu Load Dialog
# @dp.message_handler(commands='statistics', state=None)
async def cm_statistics(message : types.Message):
    if message.from_user.id == idd:
        df = audio_sqlite_db.sql_read()
        sss = df.describe(include='object').to_string()
        await bot.send_message(message.from_user.id, sss, reply_markup=admin_kb.button_case_admin)
    
# Handlers Registration
def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(cm_statistics, commands='statistics')
    dp.register_message_handler(moderator_command, commands=['moderator'], is_chat_admin=True)