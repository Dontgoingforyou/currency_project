import requests
from background_task import background

from currency.models import CurrencyRate



@background(schedule=10)
def fetch_usd_to_rub():
    """
        Запрашивает текущий курс доллара к рублю через API и сохраняет его в базе данных.
        Функция выполняется в фоновом режиме каждые 10 секунд. Если в базе данных
        содержится более 10 записей, то удаляется самая старая запись, чтобы сохранять только последние 10
        """
    API_URL = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(API_URL)
    data = response.json()
    rate = data.get('rates').get('RUB')
    if rate:
        CurrencyRate.objects.create(rate=rate)

        if CurrencyRate.objects.count() > 10:
            CurrencyRate.objects.order_by('timestamp').first().delete()
    return rate