from django.db import models
from django.core.validators import MinLengthValidator


class Account(models.Model):
    account_number = models.CharField(
        validators=[MinLengthValidator(16)],
        max_length=16,
        unique=True
    )
    balance = models.PositiveIntegerField()
    owner = models.ForeignKey('person.Person', on_delete = models.CASCADE)