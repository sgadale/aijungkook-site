from django_distill import distill_path
from . import views

urlpatterns = [
    distill_path(
        '',
        views.event_list,
        name='event_list'
    ),
]
