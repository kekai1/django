from django.contrib import admin
from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'create_at', 'create_up', 'category', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'id',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category', 'title')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)



