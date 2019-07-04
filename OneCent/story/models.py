from django.db import models
from datetime import date
from markdown import markdown


class Story(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(default=date.today)
    author = models.ForeignKey("auth.User", null=True, on_delete=models.SET_NULL)

    image = models.ImageField(blank=True, upload_to="visual_vibes")
    artwork = models.CharField(max_length=200)
    art_link = models.URLField(blank=True)
    music = models.CharField(max_length=200)
    music_link = models.URLField(blank=True)

    body = models.TextField()
    motifs = models.CharField(max_length=100)
    lit_dev = models.CharField(max_length=100)
    notes = models.TextField(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "stories"
        ordering = ["-id"]

    def save(self, *args, **kwargs):
        self.body = markdown(self.body)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
