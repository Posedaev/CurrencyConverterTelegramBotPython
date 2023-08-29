import telebot
from currency_bot.List_of_Currencies import Values
from currency_bot.User_id_Storage import Storage
from Convert import Convertate
from currency_bot.Secret import bot_token
from currency_bot.Available_Currencies import Cur


class OffTheList(BaseException):
    def __init__(self):
        pass


class SameCurrencies(BaseException):
    def __init__(self):
        pass


class Text_handler:
    @staticmethod
    def user_handler(message, text):
        user_id = message.from_user.id
        text = text.strip().upper()
        text_split = text.split()
        bot = Bot().bot
        try:
            if text_split[0] != text_split[1] in Cur.available_cur and text_split[2] and len(text_split) == 3:
                Storage().update_from(user_id, text_split[0])
                Storage().update_to(user_id, text_split[1])
                Storage().update_amount(user_id, text_split[2])
                user_storage = Storage().read(user_id)
                bot.send_message(message.chat.id, Convertate().convert(user_storage['conv_from'], user_storage['conv_to'], user_storage['amount']))
            elif (text_split[0] == text_split[1] in Cur.available_cur) and text_split[2]:
                raise SameCurrencies
            elif text_split[0].isalpha() == text_split[1].isalpha() and (text_split[0] in Cur.available_cur) and type(text_split[2]) is float or int:
                raise IndexError
            else:
                bot.send_message(message.chat.id, "Проверьте правильность введенных данных и повторите попытку снова: ")
        except IndexError:
            bot.send_message(message.chat.id, "Проверьте правильность введенных данных и повторите попытку снова: ")
        except SameCurrencies:
            bot.send_message(message.chat.id, "Зачем конвертировать одинаковые валюты?")


class Bot:
    def __init__(self):
        self.bot = telebot.TeleBot(f"{bot_token}")
        self.Conv = Convertate()
        self.storage = Storage()
        self.lst = Values(self.bot)

    def start(self):
        @self.bot.message_handler(commands=['list'])
        def on_list(message):
            lst_cur = Values(self.bot)
            lst_cur.list_of_currencies(message)

        @self.bot.message_handler(commands=['start', 'help'])
        def on_start(message):
            Storage().clear(message.from_user.id)
            self.bot.send_message(chat_id=message.chat.id, text="Введите валюту из которой хотите конвертировать, затем валюту в которую нужно конвертировать и количество.\n\nПример ввода: usd eur 100,  EUR USD 24,  usd EUR 56")

            @self.bot.message_handler(func=lambda message: True)
            def on_handler(message):
                text = message.text
                if text:
                    Text_handler.user_handler(message, text)

        self.bot.infinity_polling()


Bot().start()