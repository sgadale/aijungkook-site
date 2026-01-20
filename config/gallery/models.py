from django.db import models


class Gallery(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.URLField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
