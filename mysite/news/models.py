from django.db import models

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    create_up = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
