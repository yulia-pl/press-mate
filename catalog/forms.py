from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Newspaper, Topic, Redactor


# Форма для створення/редагування газети
class NewspaperForm(forms.ModelForm):
    class Meta:
        model = Newspaper
        fields = ["title", "content", "published_date", "topics", "redactors"]

    redactors = forms.ModelMultipleChoiceField(
        queryset=Redactor.objects.all(),  # Додаємо всіх редакторів
        widget=forms.CheckboxSelectMultiple  # Вибір кількох редакторів
    )


# Форма для створення/редагування теми
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["name"]


# Форма для редагування редактора
class RedactorForm(forms.ModelForm):
    class Meta:
        model = Redactor
        # Поля для редагування
        fields = \
            ["username", "email", "first_name", "last_name", "years_of_experience"]

# Реєстрація
class RedactorRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Redactor
        fields = ["username", "email", "first_name",
                  "last_name", "password1", "password2"]
