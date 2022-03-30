from django.shortcuts import render, get_object_or_404
from .models import *

def index(request):
    news = News.objects.order_by('-create_at')
    context = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, 'news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    this_category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'title': 'Категории',
        'this_category': this_category
    }
    return render(request, 'news/category.html', context=context)


def view_news(request,news_id):
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {'news_item': news_item})
