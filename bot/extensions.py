import json
import requests
from config import keys


class APIException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote:str, base:str, amount:str):

        if quote == base:
            raise APIException(f'невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'не удалось обработать валюту{quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'не удалось обработать валюту{base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'неверно введено колличество {amount}')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_quote = json.loads(r.content)[keys[base]]

        return total_quote
