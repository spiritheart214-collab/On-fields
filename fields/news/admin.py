from django.contrib import admin
from .models import News_article, News_preview
from django.utils.html import format_html
from django_summernote.admin import SummernoteModelAdmin

class MySummernoteAdmin(SummernoteModelAdmin):
    exclude = ('attachment',)

@admin.register(News_preview)
class News_previewAdmin(admin.ModelAdmin):
    list_display = "id", "title", "short_title"
    list_display_links = "id", "title", "short_title"
    ordering = "pk",
    search_fields = "title", "short_title"

@admin.register(News_article)
class News_articleAdmin(SummernoteModelAdmin):
    list_display       = "id", "title", "small_short_descr", "small_descr", "pub_date", "show_photo", "preview"
    list_display_links = "id", "title", "small_short_descr", "small_descr", "pub_date", "show_photo"
    ordering = "pk",
    readonly_fields = ("show_photo",)
    search_fields = "title", "small_short_descr", "preview"
    
    summernote_fields = ('descr',)
    
    def small_short_descr(self, obj : News_article) -> str:
        if len(obj.short_descr) < 48:
            return obj.short_descr
        return obj.short_descr[:48] + "..."
    small_short_descr.short_description = 'Краткое описание'
    
    def small_descr(self, obj : News_article) -> str:
        if len(obj.descr) < 48:
            return obj.descr
        return obj.descr[:48] + "..."
    small_descr.short_description = "Описание"

    def show_photo(self, obj : News_article) -> str:
        return format_html('<img src="{}" width="50" height="50" />', obj.photo.url)
    show_photo.short_description = 'Фото'
    
