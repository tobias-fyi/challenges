from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import OrderForm
from .forms import OrderFormForm


def orderform(request):
    if request.method == "POST":
        form = OrderFormForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Order submitted.")
            return redirect("sendit")

    else:
        form = OrderFormForm()

    return render(request, "former/orderform.html", {"form": form})


def sendit(request):
    template = "former/sendit.html"
    context = {"orderform": OrderForm.objects.all()}
    return render(request, template, context)


def sendit_detail(request, orderform_id):
    order = get_object_or_404(OrderForm, pk=orderform_id)
    return render(request, "former/sendit_detail.html", {"order": order})
