import typing as t

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()
SUPPORTED_FIAT_LIST = (
    "USD",
    "GBP",
    "JPY",
    "CNY",
    "EUR",
)
SUPPORTED_CRYPTOCURRENCY_LIST = ("Ethereum",)
SUPPORTED_CURRENCY_LIST = SUPPORTED_FIAT_LIST + SUPPORTED_CRYPTOCURRENCY_LIST
SUPPORTED_CURRENCIES = tuple(
    (
        (
            idx,
            c,
        )
        for idx, c in enumerate(SUPPORTED_CURRENCY_LIST)
    )
)
SUPPORTED_CURRENCIES_MAPPING = {v: k for k, v in dict(SUPPORTED_CURRENCIES).items()}


class PayProfile(models.Model):
    user = models.OneToOneField(
        UserModel, on_delete=models.CASCADE, related_name="pay_profile"
    )


class Currency(models.Model):
    name = models.IntegerField(
        name="currency_name",
        choices=SUPPORTED_CURRENCIES,
        default=0,
    )
    _balance = models.TextField(default="0")
    pay_profile = models.ForeignKey(
        PayProfile, on_delete=models.CASCADE, related_name="currencies"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "pay_profile"], name="unique_profile"
            )
        ]

    @property
    def balance(self) -> t.Union[float, int]:
        try:
            return int(self._balance) / self.scale
        except ValueError:
            self._balance = "0"
            self.save()
            return 0

    @balance.setter
    def balance(self, value: t.Union[float, int]):
        self._balance = str(int(value * self.scale))

    @property
    def scale(self):
        return settings.PAY_FIAT_SCALE if self.is_fiat else settings.PAY_SCALE

    @property
    def is_fiat(self):
        return dict(SUPPORTED_CURRENCIES).get(self.name) in SUPPORTED_FIAT_LIST
