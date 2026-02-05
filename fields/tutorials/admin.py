from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import Tutorial, Tutorial_subsection, Article
from django.utils.html import format_html
from django_summernote.admin import SummernoteModelAdmin

class MySummernoteAdmin(SummernoteModelAdmin):
    exclude = ('attachment',)

# Сокращенный вывод текста и отрисовка фото
@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = "id", "title", "small_short_descr", "small_descr", "show_photo"
    list_display_links = "id", "title", "small_short_descr", "small_descr", "show_photo"
    ordering = "pk",
    readonly_fields = ("show_photo",)
    search_fields = "title", "short_descr","descr",
    
    
    # Сокращение вывода информации и определение заголовка на русском
    def small_short_descr(self, obj : Tutorial) -> str:
        if len(obj.short_descr) < 48:
            return obj.short_descr
        return obj.short_descr[:48] + "..."
    small_short_descr.short_description = 'Краткое описание'
    
    def small_descr(self, obj : Tutorial) -> str:
        if len(obj.descr) < 48:
            return obj.descr
        return obj.descr[:48] + "..."
    small_descr.short_description = "Описание"
    
    # Отрисовка фото в админке
    def show_photo(self, obj : Tutorial) -> str:
        return format_html('<img src="{}" width="50" height="50" />', obj.photo.url)
    show_photo.short_description = 'Фото'
    
# Функция переименования, подгрузка одним запросом
@admin.register(Tutorial_subsection)
class Tutorial_subsectionAdmin(admin.ModelAdmin):
    list_display       = "id", "title", "small_short_descr", "small_descr", "tutorial", 
    list_display_links = "id", "title", "small_short_descr", "small_descr",
    ordering = "pk",
    search_fields = "title", "short_descr",
    
    def small_short_descr(self, obj : Tutorial_subsection) -> str:
        if len(obj.short_descr) < 48:
            return obj.short_descr
        return obj.short_descr[:48] + "..."
    small_short_descr.short_description = 'Краткое описание'
    
    def small_descr(self, obj : Tutorial_subsection) -> str:
        if len(obj.descr) < 48:
            return obj.descr
        return obj.descr[:48] + "..."
    small_descr.short_description = "Описание"
    
    # Переименование связи через функцию
    def tutorial(self, obj):
        return obj.id_tutorial.title
    tutorial.short_description = 'От раздела'
    
    # Подгрузка всех связей одним запросом
    def get_queryset(self, request: HttpRequest):
        return super().get_queryset(request).select_related("id_tutorial")
    
@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    list_display       = "id", "title", "small_short_descr", "small_descr", "pub_date", "sub_tutorial",
    list_display_links = "id", "title", "small_short_descr", "small_descr", "pub_date",
    ordering = "pk",
    search_fields = "title", "short_descr",
    
    summernote_fields = ('descr',)
    
    def small_short_descr(self, obj : Article) -> str:
        if len(obj.short_descr) < 48:
            return obj.short_descr
        return obj.short_descr[:48] + "..."
    small_short_descr.short_description = 'Краткое описание'
    
    def small_descr(self, obj : Article) -> str:
        if len(obj.descr) < 48:
            return obj.descr
        return obj.descr[:48] + "..."
    small_descr.short_description = "Описание"
    
    def sub_tutorial(self, obj):
        return obj.id_subsection.title
    sub_tutorial.short_description = 'От подраздела'
    
    def get_queryset(self, request: HttpRequest):
        return super().get_queryset(request).select_related("id_subsection")
