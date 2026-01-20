from django.shortcuts import render
from .models import Gallery


def gallery_list(request):
    images = Gallery.objects.all()
    return render(request, 'gallery/gallery_list.html', {'images': images})
