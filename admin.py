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
        #print(df)
        # convert the 'date' column to a datetime object
        # df[['use_date']] = pd.to_datetime(df[['use_date']], format="%Y-%m-%d %H:%M:%S")
        #.astype('datetime64[ns]'.strftime('%Y-%m-%d %H:%M:%s'))
        #print(print(df.reset_index()[['use_date', format("%Y-%m-%d %H:%M:%s"), 'user_name', 'action']]))
        
        #buf = io.StringIO()
        #df.info(buf=buf)
        #sss = buf.getvalue()
        sss = df.describe(include='object').to_string()
        #print(df.describe(include='object'))
        bbuf = str(df[['use_date', 'user_name', 'action']]) + '\n-------------------------\n' + sss
        await bot.send_message(message.from_user.id, bbuf, reply_markup=admin_kb.button_case_admin)
    
# Handlers Registration
def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(cm_statistics, commands='statistics')
    dp.register_message_handler(moderator_command, commands=['moderator'], is_chat_admin=True)