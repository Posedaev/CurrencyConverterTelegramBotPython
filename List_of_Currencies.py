from datetime import datetime
from currency_bot.User_id_Storage import Storage
from currency_bot.Secret import api_key
import requests
import json


class Values:
    def __init__(self, bot):
        self.bot = bot
        self.storage = Storage()

    def list_of_currencies(self, message):
        result = requests.get(f"https://api.exchangerate.host/&{api_key}?base=RUB")
        response = json.loads(result.content)['rates']
        lst = ', '.join(response)
        self.bot.send_message(message.chat.id, f"Доступные курсы\nна {datetime.today()}\n{lst}: ")