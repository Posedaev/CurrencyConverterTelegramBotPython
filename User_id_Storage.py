import json
import os


class Storage:
    def update_from(self, user_id, value):
        if value.isalpha():
            data = self.read(user_id)
            data['conv_from'] = value
            with open("Database/user_" + str(user_id), 'w') as file:
                json.dump(data, file)
        else:
            raise IndexError

    def update_to(self, user_id, value):
        if value.isalpha():
            data = self.read(user_id)
            data['conv_to'] = value
            with open("Database/user_" + str(user_id), 'w') as file:
                json.dump(data, file)
        else:
            raise IndexError

    def update_amount(self, user_id, value):
        str(value)
        data = self.read(user_id)
        data['amount'] = value
        with open("Database/user_" + str(user_id), 'w') as file:
            json.dump(data, file)

    def read(self, user_id):
        try:
            with open("Database/user_" + str(user_id), 'r') as file:
                data = file.read()
                return json.loads(data)
        except FileNotFoundError:
            return {'conv_from': None, 'conv_to': None, "amount": None}

    def clear(self, user_id):
        try:
            os.remove("Database/user_" + str(user_id))
        except FileNotFoundError:
            pass