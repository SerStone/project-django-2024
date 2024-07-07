import json
import os
from datetime import datetime, timedelta

import requests

from .models import ExchangeRate

CACHE_FILE = 'exchange_rates.json'
CACHE_EXPIRATION = timedelta(days=1)


def get_exchange_rates():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as file:
            data = json.load(file)
            last_updated = datetime.fromisoformat(data['last_updated'])
            if datetime.now() - last_updated < CACHE_EXPIRATION:
                return data['rates']

    response = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
    rates = response.json()
    data = {
        'last_updated': datetime.now().isoformat(),
        'rates': rates
    }
    with open(CACHE_FILE, 'w') as file:
        json.dump(data, file)

    save_exchange_rates(rates)

    return rates


def save_exchange_rates(rates):
    ExchangeRate.objects.all().delete()

    for rate in rates:
        ExchangeRate.objects.create(
            currency=rate['ccy'],
            base_currency=rate['base_ccy'],
            buy=rate['buy'],
            sale=rate['sale']
        )
