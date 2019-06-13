from django.forms import ModelForm
from .models import OrderForm


class OrderFormForm(ModelForm):
    class Meta:
        model = OrderForm
        fields = (
            "date_requested",
            "phone",
            "email",
            "address",
            "city",
            "state_code",
            "zip_code",
        )
