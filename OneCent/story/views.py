from django.views.generic import TemplateView, ListView, DetailView
from django.core.paginator import Paginator

from .models import Story


class StoryIndexView(ListView):
    template_name = "index.html"
    model = Story
    context_object_name = "stories"
    paginate_by = 4


class StoryDetailView(DetailView):
    template_name = "detail.html"
    model = Story
    context_object_name = "story"


class AboutView(TemplateView):
    template_name = "about.html"
