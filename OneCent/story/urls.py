from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import StoryIndexView, StoryDetailView


urlpatterns = [
    path("story/<int:pk>/", StoryDetailView.as_view(), name="story_detail"),
    path("", StoryIndexView.as_view(), name="story_list"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
