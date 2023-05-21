import json

from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher

file = open('/home/pavel/cfg/config.json', 'r')
config = json.load(file)

storage = MemoryStorage()

bot = Bot(token = config['rtlab_voice_bot_token'])
dp = Dispatcher(bot, storage=storage)

global_lang = 'ru'