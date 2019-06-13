from django.db import models
from django.utils import timezone


class OrderForm(models.Model):
    date_requested = models.DateTimeField(default=timezone.now)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=140)
    city = models.CharField(max_length=80)
    state_code = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return self.email
