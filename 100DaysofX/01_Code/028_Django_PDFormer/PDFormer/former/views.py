from django.http import HttpResponse


def formpage(request):
    return HttpResponse("Hello there, here are some form fields.")
