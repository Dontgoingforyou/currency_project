import time

from django.http import JsonResponse

from currency.models import CurrencyRate
from currency.utils import fetch_usd_to_rub


def get_current_usd(request):
    time.sleep(10)
    rate = fetch_usd_to_rub()

    history = CurrencyRate.objects.order_by('-timestamp')[:10]
    history_data = [{
        'rate': entry.rate,
        'timestamp': entry.timestamp,
    } for entry in history]

    return JsonResponse({'current_rate': rate, 'history': history_data})
