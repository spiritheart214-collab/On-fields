from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = "id", "questions", "answer"
    list_display_links = "id", "questions", "answer"
    ordering = "pk",
    search_fields = "questions",
    