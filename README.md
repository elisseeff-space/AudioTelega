# AudioTelega
 Try to get Audio from Telegram Bot

export PYTHONPATH="/home/pavel/github/AudioTelega"
export PYTHONPATH="/home/pavel/github/AudioTelega/venv/lib/python3.10/site-packages"

export GOOGLE_APPLICATION_CREDENTIALS="/home/pavel/tokens/zinc-fusion-386715-60a5226fadb5.json"

Credentials saved to file: [/home/pavel/.config/gcloud/application_default_credentials.json]

These credentials will be used by any library that requests Application Default Credentials (ADC).

Quota project "zinc-fusion-386715" was added to ADC which can be used by Google client libraries for billing and quota. Note that some services may still bill the project owning the resource.

virtualenv venv
source venv/bin/activate



# Хэндлер на получение голосового и аудио сообщения
@dp.message_handler(content_types=[
    types.ContentType.VOICE,
    types.ContentType.AUDIO,
    types.ContentType.DOCUMENT
    ]
)
async def voice_message_handler(message: types.Message):
    """
    Обработчик на получение голосового и аудио сообщения.
    """
    if message.content_type == types.ContentType.VOICE:
        file_id = message.voice.file_id
    elif message.content_type == types.ContentType.AUDIO:
        file_id = message.audio.file_id
    elif message.content_type == types.ContentType.DOCUMENT:
        file_id = message.document.file_id
    else:
        await message.reply("Формат документа не поддерживается")
        return

    file = await bot.get_file(file_id)
    file_path = file.file_path
    file_on_disk = Path("", f"{file_id}.tmp")
    await bot.download_file(file_path, destination=file_on_disk)
    await message.reply("Аудио получено")

    text = stt.audio_to_text(file_on_disk)
    if not text:
        text = "Формат документа не поддерживается"
    await message.answer(text)

    os.remove(file_on_disk)  # Удаление временного файла

    # do something with the audio file
    logging.warning("Audio file getted succesful!")
    # await bot.send_message(message.from_user.id, 'Hello {0.first_name}. Audio file is read!'.format(message.from_user))

# Хэндлер на команду /start , /help
@dp.message_handler(commands=["start", "help"])
async def cmd_start(message: types.Message):
    print(stt.audio_to_text("audio_2023-04-23_07-33-17.ogg"))
    await message.reply(
        "Привет! Это Бот для конвертации голосового/аудио сообщения в текст"
        " и создания аудио из текста."
    )

# Хэндлер на команду /test
@dp.message_handler(commands="test")
async def cmd_test(message: types.Message):
    """
    Обработчик команды /test
    """
    await message.answer("Test")

# Start the bot
if __name__ == '__main__':
    try:
        executor.start_polling(dp, skip_updates=True)
    except (KeyboardInterrupt, SystemExit):
        pass