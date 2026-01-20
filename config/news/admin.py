from django.contrib import admin
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'published_date',
        'is_featured',
    )
    list_filter = ('is_featured', 'published_date')
    search_fields = ('title',)
    ordering = ('-published_date',)
