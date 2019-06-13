from django.urls import path
from . import views


urlpatterns = [
    path("", views.orderform, name="orderform"),
    path("sendit/", views.sendit, name="sendit"),
    path(
        "sendit/<int:orderform_id>/", views.sendit_detail, name="sendit_detail"
    ),
]
