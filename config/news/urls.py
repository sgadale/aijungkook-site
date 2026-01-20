from django.urls import path
from django_distill import distill_path
from . import views
from .models import News


def get_news_slugs():
    return [
        {'slug': slug}
        for slug in News.objects.values_list('slug', flat=True)
    ]


urlpatterns = [
    distill_path(
        '',
        views.news_list,
        name='news_list'
    ),

    distill_path(
        '<slug:slug>/',
        views.news_detail,
        name='news_detail',
        distill_func=get_news_slugs
    ),
]
