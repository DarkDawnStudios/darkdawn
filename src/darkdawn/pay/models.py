from django.db import models
from django.contrib.auth import get_user_model
import decimal

user_model = get_user_model()

class Balance(models.Model):
    user = models.OneToOneField(
        user_model, on_delete=models.CASCADE, related_name="balance"
    )
    usd100x = models.BigIntegerField(default=0)
    @property
    def usd(self):
        return str(decimal.Decimal(str(self.usd100x)) / 100)
