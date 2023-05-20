import logging
import os, json
#from pathlib import Path

from create_bot import dp
from aiogram.utils import executor
from handlers import client, admin, other
#from aiogram.types import Message, Audio
from datetime import datetime

logger = logging.getLogger(__name__)
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
    logging.warning("Elisseeff Audio Bot logging is ON!")
    #sqllite_db.sql_start()

# Start the bot
if __name__ == '__main__':
    try:
        executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    except (KeyboardInterrupt, SystemExit):
        pass