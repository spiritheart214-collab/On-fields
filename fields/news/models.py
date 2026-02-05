from django.db import models
from datetime import datetime
from django.utils.text import slugify
from unidecode import unidecode


#НОВОСТИ И СТАТЬИ
#-------------------------------------------------------------
class News_preview(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    short_title = models.CharField('Краткий заголовок', max_length=200)
     
    class Meta:
        ordering = ["title"]
        verbose_name = "id"
        verbose_name_plural = "ids"

    def __str__(self):
        return self.title
    
#Статьи
class News_article(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    short_descr = models.CharField('Краткое описание', max_length=500)
    descr = models.TextField('Описание')
    pub_date = models.DateTimeField('Время публикации', default=datetime.now)
    preview = models.ForeignKey(News_preview, on_delete=models.CASCADE, verbose_name='язык')
    photo = models.ImageField('Фото', upload_to='news_&_articles/')
     # Новое поле для хранения транслитерированной версии заголовка
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)
        # Переводим slug на английский язык и заменяем пробелы на символы "-" или "_"
        new_slug = slugify(unidecode(self.title))
        if self.slug != new_slug:
            self.slug = new_slug
            self.save()