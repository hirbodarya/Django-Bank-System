from django.db import models
from django.core.validators import MinLengthValidator


class Person(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    national_id = models.CharField(
        validators=[MinLengthValidator(10)],
        max_length = 10,
        unique = True
    )