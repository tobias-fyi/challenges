from django.views.generic import ListView, DetailView

from .models import Story


class StoryIndexView(ListView):
    model = Story
    context_object_name = "stories"
    template_name = "index.html"


class StoryDetailView(DetailView):
    model = Story
    context_object_name = "story"
    template_name = "detail.html"
