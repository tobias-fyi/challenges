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

    def get_context_data(self, **kwargs):
        """Adds to context a count of Story objects."""
        context = super().get_context_data(**kwargs)
        context["count"] = Story.objects.count()
        print(context["count"])
        return context


class AboutView(TemplateView):
    template_name = "about.html"
