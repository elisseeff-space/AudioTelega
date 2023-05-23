# AudioTelega
 Try to get Audio from Telegram Bot

export PYTHONPATH="/home/pavel/github/AudioTelega"
export PYTHONPATH="/home/pavel/AudioTelega"
export PYTHONPATH="/home/pavel/github/AudioTelega/venv/lib/python3.10/site-packages"

export GOOGLE_APPLICATION_CREDENTIALS="/home/pavel/tokens/zinc-fusion-386715-60a5226fadb5.json"

Credentials saved to file: [/home/pavel/.config/gcloud/application_default_credentials.json]

These credentials will be used by any library that requests Application Default Credentials (ADC).

Quota project "zinc-fusion-386715" was added to ADC which can be used by Google client libraries for billing and quota. Note that some services may still bill the project owning the resource.

virtualenv venv
source venv/bin/activate

pip install google-cloud-speech
pip install aiogram
pip install pandas



# Хэндлер на получение голосового и аудио сообщения
@dp.message_handler(content_types=[
    types.ContentType.VOICE,
    types.ContentType.AUDIO,
    types.ContentType.DOCUMENT
    ]
)


# Start the bot
if __name__ == '__main__':
    try:
        executor.start_polling(dp, skip_updates=True)
    except (KeyboardInterrupt, SystemExit):
        pass