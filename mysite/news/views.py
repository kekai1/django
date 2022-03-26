from django.shortcuts import render
from .models import News

def index(request):
    news = News.objects.order_by('-create_at')
    context = {
        'news': news,
        'title': 'Список новостей'
    }

    return render(request, 'news/base.html', context=context)