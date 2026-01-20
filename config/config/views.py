from django.shortcuts import render
from members.models import Member
from news.models import News
from events.models import Event


def home(request):
    members = Member.objects.filter(is_active=True)[:6]
    featured_news = News.objects.filter(is_featured=True)[:3]
    upcoming_events = Event.objects.order_by('date')[:3]

    context = {
        'members': members,
        'featured_news': featured_news,
        'upcoming_events': upcoming_events,
    }

    return render(request, 'home.html', context)
