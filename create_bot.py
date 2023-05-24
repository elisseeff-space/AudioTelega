import json

from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher

file = open('/home/pavel/cfg/config.json', 'r')
config = json.load(file)

storage = MemoryStorage()

class BotLanguage:
    def __init__(self, lang):
        self.lang = lang
    def set(self, lang):
        self.lang = lang
    def get(self):
        return self.lang

my_lang = BotLanguage('ru')

bot = Bot(token = config['rtlab_voice_bot_token'])
#bot = Bot(token = config['VoskModelSTT_bot'])

dp = Dispatcher(bot, storage=storage)