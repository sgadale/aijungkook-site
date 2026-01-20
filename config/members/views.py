from django.shortcuts import render, get_object_or_404
from .models import Member


def member_list(request):
    members = Member.objects.filter(is_active=True)
    return render(request, 'members/member_list.html', {'members': members})


def member_detail(request, slug):
    member = get_object_or_404(Member, slug=slug, is_active=True)
    return render(request, 'members/member_detail.html', {'member': member})
