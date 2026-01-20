from django.contrib import admin
from .models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'stage_name',
        'name',
        'position',
        'is_active',
    )
    list_filter = ('is_active',)
    search_fields = ('name', 'stage_name', 'position')
    ordering = ('stage_name',)
