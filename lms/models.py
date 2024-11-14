from django.db import models
from config import settings

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=30, verbose_name='название')
    preview = models.ImageField(upload_to='course/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='автор', **NULLABLE)
    product_id = models.CharField(max_length=100, verbose_name='id продукта в stripe', **NULLABLE)
    price_id = models.CharField(max_length=100, verbose_name='id цены в stripe', **NULLABLE)
    pay_id = models.CharField(max_length=100, verbose_name='id сессии оплаты', **NULLABLE)
    usd_price = models.IntegerField(verbose_name='цена в $', **NULLABLE)

    def __str__(self):
        return f'Курс {self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=30, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='lesson/', verbose_name='превью', **NULLABLE)
    video_url = models.URLField(verbose_name='ссылка на видео', **NULLABLE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='автор', **NULLABLE)
    product_id = models.CharField(max_length=100, verbose_name='id продукта в stripe', **NULLABLE)
    price_id = models.CharField(max_length=100, verbose_name='id цены в stripe', **NULLABLE)
    pay_id = models.CharField(max_length=100, verbose_name='id сессии оплаты', **NULLABLE)
    usd_price = models.IntegerField(verbose_name='цена в $', **NULLABLE)

    def __str__(self):
        return f'Урок {self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'