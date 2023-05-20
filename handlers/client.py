from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove, ContentType, File, Message
from data_base import audio_sqlite_db
from google_stt import elis_google_stt
from pathlib import Path

#@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приветствую Вас в моей картинной галерее!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через личку. Напишите ему:\nhttps://t.me/elis_gallery_bot')

async def handle_file(file: File, file_name: str, path: str):
    Path(f"{path}").mkdir(parents=True, exist_ok=True)

    await bot.download_file(file_path=file.file_path, destination=f"{path}/{file_name}")

# @dp.message_handler(content_types=[ContentType.VOICE])
async def voice_message_handler(message: Message): # types.Message):
    # Get the file ID of the voice message
    voice = await message.voice.get_file()
    path = "/home/pavel/github/AudioTelega/voices"

    await handle_file(file=voice, file_name=f"{voice.file_id}.ogg", path=path)
    
    file_name = path + f"/{voice.file_id}.ogg"
    result = elis_google_stt.transcribe_file(file_name)
    await message.reply("Transcript: {}".format(result.alternatives[0].transcript))

    #print('Everything Allright!')
    await audio_sqlite_db.use_log_add_command(message.from_user.username, message.from_user.id, 'Voice message' )

async def working_time_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Работает круглый сутки! Приходите все!')

async def destination_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Blumenstrasse, 13!', reply_markup=ReplyKeyboardRemove())

async def gallery_menu_command(message : types.Message):
    #await sqllite_db.sql_read(message)
    await bot.send_message(message.from_user.id, 'Blumenstrasse, 13!')


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(voice_message_handler, content_types=[
    types.ContentType.VOICE,
    types.ContentType.AUDIO,
    types.ContentType.DOCUMENT
    ])
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(working_time_command, commands=['working_time'])
    dp.register_message_handler(destination_command, commands=['destination'])
    dp.register_message_handler(gallery_menu_command, commands=['gallery'])