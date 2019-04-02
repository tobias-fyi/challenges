from django.db import models
from django.utils import timezone


class OrderForm(models.Model):
    date_requested = models.DateTimeField(default=timezone.now)
    phone = models.PositiveIntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=140)
    city = models.CharField(max_length=80)
    state = models.CharField(max_length=2)
    zip_code = models.PositiveIntegerField()
