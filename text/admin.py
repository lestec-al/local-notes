from django.contrib import admin
from text import models


@admin.register(models.Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]