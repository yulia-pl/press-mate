from django.contrib import admin
from .models import Topic, Newspaper, Redactor


# Реєстрація моделі Topic
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


# Реєстрація моделі Redactor
@admin.register(Redactor)
class RedactorAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "years_of_experience")
    search_fields = ("username", "email")
    list_filter = ("years_of_experience",)


# Реєстрація моделі Newspaper
@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    list_display = ("title", "published_date")
    search_fields = ("title", "content")
    list_filter = ("published_date",)
    filter_horizontal = ("topics", "redactors")  # можливість вибору редакторів
