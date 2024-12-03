from django.shortcuts import render
from .models import Newspaper, Topic, Redactor

# В'юшка для відображення списку газет
def newspaper_list(request):
    newspapers = Newspaper.objects.all()  # Отримуємо всі газети
    return render(request, "newspaper_list.html", {"newspapers": newspapers})

# В'юшка для відображення деталей газети
def newspaper_detail(request, pk):
    newspaper = Newspaper.objects.get(pk=pk)  # Отримуємо газету за pk
    return render(request, "newspaper_detail.html", {"newspaper": newspaper})

# В'юшка для відображення списку тем
def topic_list(request):
    topics = Topic.objects.all()  # Отримуємо всі теми
    return render(request, "topic_list.html", {"topics": topics})

# В'юшка для відображення списку редакторів
def redactor_list(request):
    redactors = Redactor.objects.all()  # Отримуємо всіх редакторів
    return render(request, "redactor_list.html", {"redactors": redactors})
