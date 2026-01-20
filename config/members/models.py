from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=100)
    stage_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['stage_name']

    def __str__(self):
        return self.stage_name
