from django.db import models
from django.utils.text import slugify

class Article(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
            super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id} - {self.title}"
