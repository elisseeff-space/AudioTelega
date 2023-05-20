from aiogram import Bot

from aiogram.dispatcher import Dispatcher
import json
from aiogram.contrib.fsm_storage.memory import MemoryStorage

file = open('/home/pavel/cfg/config.json', 'r')
config = json.load(file)

storage = MemoryStorage()

bot = Bot(token = config['rtlab_voice_bot_token'])
dp = Dispatcher(bot, storage=storage)

global_lang = 'ru'