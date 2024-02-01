from django.db import models


class Gallery(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    dimensions = models.CharField(max_length=20)
    image = models.URLField(max_length=255, default=None)
    published = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
