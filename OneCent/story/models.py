from django.db import models


class Story(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("auth.User", null=True, on_delete=models.SET_NULL)
    body = models.TextField()
    motifs = models.CharField(max_length=100)
    lit_dev = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    vibe = models.ManyToManyField("Vibrary")

    class Meta:
        verbose_name_plural = "stories"

    def __str__(self):
        return self.title


class Vibrary(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    vibe_type = models.CharField(max_length=50)
    link = models.URLField(blank=True)
    image = models.ImageField(blank=True, upload_to="visual_vibes")
    notes = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "vibes"
        ordering = ["vibe_type", "author", "title"]

    def __str__(self):
        return self.title
