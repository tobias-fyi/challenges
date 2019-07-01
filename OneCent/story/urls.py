from django.urls import path

from .views import StoryIndexView, StoryDetailView


urlpatterns = [
    path("story/<int:pk>/", StoryDetailView.as_view(), name="story_detail"),
    path("", StoryIndexView.as_view(), name="story_list"),
]
