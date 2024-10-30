from background_task.models import Task
from django.http import JsonResponse

from currency.models import CurrencyRate
from currency.utils import fetch_usd_to_rub


def get_current_usd(request):
    """
        Возвращает текущий курс доллара к рублю и историю последних 10 записей.
        Если задача обновления курса еще не запланирована, функция вызывает fetch_usd_to_rub()
        для добавления задачи. История курса возвращается в формате JSON.
        """
    print("Проверка на существование задачи")
    if not Task.objects.filter(task_name='currency.utils.fetch_usd_to_rub').exists():
        print("Задача не найдена. Запуск функции fetch_usd_to_rub.")
        fetch_usd_to_rub()
    else:
        print("Задача уже запланирована.")
    history = CurrencyRate.objects.order_by('-timestamp')[:10]
    history_data = [{
        'rate': entry.rate,
        'timestamp': entry.timestamp,
    } for entry in history]

    return JsonResponse({'history': history_data})
