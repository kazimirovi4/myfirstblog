from django.conf import settings
from django.db import models
from django.utils import timezone

class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор статьи')
    title = models.CharField('Название статьи', max_length=150)
    text = models.TextField('Текст статьи')
    create_date = models.DateTimeField('Дата создания', default=timezone.now)
    pub_date = models.DateTimeField('Дата публикации', blank=True, null=True)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author_name = models.CharField('Имя коментатора', max_length=50)
    text = models.CharField('Текст комментария', max_length=300)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'