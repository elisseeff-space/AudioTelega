import audio_sqlite_db
from elis_google_stt import transcribe_file
from pathlib import Path
from aiogram import Dispatcher, types
from aiogram.types import ContentType, File, Message, ReplyKeyboardRemove
from create_bot import bot, dp, global_lang
from client_kb import kb_client

#@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Hi! It is voice recognition bot. You can send voice message.', reply_markup=kb_client)
        #await message.delete()
    except:
        await message.reply('Общение с ботом через личку. Напишите ему:\nhttps://t.me/rtlab_voice_bot')

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
    result = transcribe_file(file_name)
    answer_message = "@Elis_OpenAI_bot {}".format(result.alternatives[0].transcript)
    await message.reply(answer_message)
    await audio_sqlite_db.use_log_add_command(message.from_user.username, message.from_user.id, answer_message, result.language_code, float(result.alternatives[0].confidence))

async def language_ru_command(message : types.Message):
    global_lang = 'ru'
    await bot.send_message(message.from_user.id, 'Russian Language of Voice Messages.')

async def language_en_command(message : types.Message):
    global_lang = 'en'
    await bot.send_message(message.from_user.id, 'English Language of Voice Messages.')

async def language_fr_command(message : types.Message):
    global_lang = 'fr'
    await bot.send_message(message.from_user.id, 'France Language of Voice Messages.')


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(voice_message_handler, content_types=[
    types.ContentType.VOICE,
    types.ContentType.AUDIO,
    types.ContentType.DOCUMENT
    ])
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(language_ru_command, commands=['ru'])
    dp.register_message_handler(language_en_command, commands=['en'])
    dp.register_message_handler(language_fr_command, commands=['fr'])