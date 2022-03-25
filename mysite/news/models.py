from django.db import models

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    create_up = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True, verbose_name="Публикация")

    def __str__(self):
        return self.title



'''
Работа с бд через djangо консоль:
python manage.py shell


from news.models import News

вот так:
    News(title = 'Новость 1', content='Контент нашей новости')
    news = _ 
    news.save()
или так: 
    news = News(title = 'Новость 2', content='Контент нашей новости 2')
    news.save()
или так:
    news = News()
    news.title = 'Новости'
    news.content = 'Вот это новости'
    news.save()
или так:
    news = News.objects.create(title = 'Новость 2', content='Контент нашей новости 2')
или так:
    News.objects.create(title = 'Новость 2', content='Контент нашей новости 2')


После того, как запись добавлена в БД, можно "веселиться":
news1.id или news1.pk
news1.title     

     
Берем данные:
    news=News.objects.all()
    
    news=News.objects.filter(id=4)
    print(news[0].title)

    news=News.objects.get(pk=3) или news=News.objects.get(id=3)
    print(news.title)
  
Изменяем данные:    
    news=News.objects.get(pk=3)
    news.title = 'Обновлено'
    news.save()

Удаляем:
    news=News.objects.get(pk=3) 
    news.delete()

Сортируем:
    прямой порядок:
        News.objects.order_by('title') 
    обратный порядок: 
        News.objects.order_by('-title')
    берем все, кроме: 
        News.objects.exclude(title = 'News 4')
    






from django.db import connection
connection.queries

'''