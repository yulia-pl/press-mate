from django.contrib import admin
from catalog.models import Topic, Newspaper, Redactor

# Реєстрація моделі Topic
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("name",)  # Відображення назв тем
    search_fields = ("name",)  # Пошук за назвою теми


# Реєстрація моделі Redactor
@admin.register(Redactor)
class RedactorAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "years_of_experience")
    search_fields = ("username", "email")  # Пошук за ім'ям користувача та поштою
    list_filter = ("years_of_experience",)  # Фільтр за досвідом


# Реєстрація моделі Newspaper
@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    list_display = ("title", "published_date")
    search_fields = ("title", "content")  # Пошук за назвою та контентом
    list_filter = ("published_date",)  # Фільтр за датою випуску
    filter_horizontal = ("topics", "redactors")  # Зручне додавання тем та редакторів
