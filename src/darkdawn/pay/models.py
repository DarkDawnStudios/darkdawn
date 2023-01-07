import decimal
import math

from django.contrib.auth import get_user_model
from django.db import models

user_model = get_user_model()


class Balance(models.Model):
    user = models.OneToOneField(
        user_model, on_delete=models.CASCADE, related_name="balance"
    )
    usd1000x = models.BigIntegerField(default=0, null=False)

    @property
    def usd(self) -> str:
        return str(decimal.Decimal(str(self.usd1000x)) / 1000)

    def top_up(self, usd):
        usd1000x = math.ceil(usd * 1000)
        self.usd1000x += usd1000x
        self.save()
