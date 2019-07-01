from django.contrib import admin
from django.urls import path, include

urlpatterns = [path("mgmt/", admin.site.urls), path("", include("story.urls"))]
