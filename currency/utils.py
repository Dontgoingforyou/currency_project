import requests

from currency.models import CurrencyRate

API_URL = 'https://api.exchangerate-api.com/v4/latest/USD'

def fetch_usd_to_rub():
    response = requests.get(API_URL)
    data = response.json()
    rate = data.get('rates').get('RUB')
    if rate:
        CurrencyRate.objects.create(rate=rate)

        if CurrencyRate.objects.count() > 10:
            CurrencyRate.objects.order_by('timestamp').first().delete()
    return rate