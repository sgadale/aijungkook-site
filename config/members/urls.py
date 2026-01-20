from django.urls import path
from django_distill import distill_path
from . import views
from .models import Member


def get_member_slugs():
    return [
        {'slug': slug}
        for slug in Member.objects.filter(is_active=True)
                                 .values_list('slug', flat=True)
    ]


urlpatterns = [
    distill_path(
        '',
        views.member_list,
        name='member_list'
    ),

    distill_path(
        '<slug:slug>/',
        views.member_detail,
        name='member_detail',
        distill_func=get_member_slugs
    ),
]
