from django.contrib import admin
from .models import Word
# Register your models here.


class WordAdmin(admin.ModelAdmin):
    list_display = ("id", "right", "wrong", "numOfAttempts", "numOfCorrect")


admin.site.register(Word, WordAdmin)
