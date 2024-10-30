from django.db import models

class CurrencyRate(models.Model):
    rate = models.DecimalField(max_digits=10, decimal_places=4)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Курс валют'
        verbose_name_plural = 'Курсы валют'

    def __str__(self):
        return f"Доллар к рублю: {self.rate}"