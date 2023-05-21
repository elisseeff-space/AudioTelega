import logging
import json

from create_bot import dp
import data_base
from data_base import audio_sqlite_db
from aiogram.utils import executor
from handlers import client, admin, other
#from aiogram.types import Message, Audio
from datetime import datetime

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)

logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(
    level=logging.INFO,
    filename="audio_bot.log",
    format='%(asctime)s - %(levelname)s - %(message)s'
)
handler = logging.FileHandler('audio_bot.log')
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)

file = open('/home/pavel/cfg/config.json', 'r')
config = json.load(file)
#rtlab_voice_bot_token

#now = datetime.now()

async def on_startup(_):
    logger.warning("Elisseeff Audio Bot logging is ON!")
    audio_sqlite_db.sql_start(logger)

# Start the bot
if __name__ == '__main__':
    try:
        executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    except (KeyboardInterrupt, SystemExit):
        pass