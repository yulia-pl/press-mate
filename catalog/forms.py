from django import forms
from .models import Newspaper, Topic


# для створення/редагування газети
class NewspaperForm(forms.ModelForm):
    class Meta:
        model = Newspaper
        # Вибір полів для форми
        fields = ["title", "content", "published_date", "topics", "redactors"]


# для створення/редагування теми
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["name"]  # Тільки назва теми
