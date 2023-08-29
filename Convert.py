import requests
import json
from currency_bot.Secret import api_key


class Convertate:
    def convert(self, conv_from, conv_to, amount):
        result = requests.get(f"https://api.exchangerate.host/&apikey={api_key}&convert?from={conv_from}&to={conv_to}&base={conv_from}")
        if result.status_code == 200:
            data = json.loads(result.text)
            response = f"{data['rates'][conv_to]}"
            multiplication = float(response) * float(amount)
            rounded = round(multiplication, 3)
            return f"{amount} {conv_from} = {rounded} {conv_to}"
        else:
            return None