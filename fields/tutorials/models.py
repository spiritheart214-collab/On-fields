from datetime import datetime 
from django.db import models
from django.utils.text import slugify
from unidecode import unidecode

# САМОУЧИТЕЛЬ
# Раздел
class Tutorial(models.Model):

    title = models.CharField('Заголовок', max_length=100)
    short_descr = models.TextField('Краткое описание', max_length=500)
    descr = models.TextField('Описание')
    photo = models.ImageField('Фото', upload_to='tutorial/')
    slug_tutorial = models.SlugField(unique=True, blank=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug_tutorial:
            self.slug_tutorial = slugify(unidecode(self.title))
        super().save(*args, **kwargs)
        # Переводим slug на английский язык и заменяем пробелы на символы "-" или "_"
        new_slug = slugify(unidecode(self.title))
        if self.slug_tutorial != new_slug:
            self.slug_tutorial = new_slug
            self.save()
    
#Подраздел
class Tutorial_subsection(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    short_descr = models.CharField('Краткое описание', max_length=500)
    descr = models.TextField('Описание')
    id_tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE, related_name='subsections', verbose_name='Раздел')
    slug_sub_tutorial = models.SlugField(unique=True, blank=True)
    
    class Meta:
        ordering = ["title"]
        verbose_name = "Подраздел"
        verbose_name_plural = "Подразделы"

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug_sub_tutorial:
            self.slug_sub_tutorial = slugify(unidecode(self.title))
        super().save(*args, **kwargs)
        # Переводим slug на английский язык и заменяем пробелы на символы "-" или "_"
        new_slug = slugify(unidecode(self.title))
        if self.slug_sub_tutorial != new_slug:
            self.slug_sub_tutorial = new_slug
            self.save()
            
#Cтатьи
class Article(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    short_descr = models.CharField('Краткое описание', max_length=500)
    descr = models.TextField('Описание')
    pub_date = models.DateTimeField('Время публикации', default=datetime.now)
    id_subsection = models.ForeignKey(Tutorial_subsection, on_delete=models.CASCADE, related_name='articles',verbose_name='Подраздел' )
    slug_article = models.SlugField(unique=True, blank=True)
    
    class Meta:
        ordering = ["title"]
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug_article:
            self.slug_article = slugify(unidecode(self.title))
        super().save(*args, **kwargs)
        # Переводим slug на английский язык и заменяем пробелы на символы "-" или "_"
        new_slug = slugify(unidecode(self.title))
        if self.slug_article != new_slug:
            self.slug_article = new_slug
            self.save()