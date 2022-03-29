from django.shortcuts import render
from .models import *

def index(request):
    news = News.objects.order_by('-create_at')
    category = Category.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
        'category': category
    }
    return render(request, 'news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.all()
    this_category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'title': 'Категории',
        'category': category,
        'this_category': this_category
    }
    return render(request, 'news/category.html', context=context)


