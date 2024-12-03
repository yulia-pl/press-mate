from django.shortcuts import render, get_object_or_404, redirect
from .models import Newspaper, Topic, Redactor
from .forms import NewspaperForm, TopicForm, RedactorForm


# відображення списку газет
def newspaper_list(request):
    newspapers = Newspaper.objects.all()  # Отримуємо всі газети
    return render(request, "newspaper_list.html", {"newspapers": newspapers})


# відображення деталей газети
def newspaper_detail(request, pk):
    newspaper = Newspaper.objects.get(pk=pk)  # Отримуємо газету за pk
    return render(request, "newspaper_detail.html", {"newspaper": newspaper})


# відображення списку тем
def topic_list(request):
    topics = Topic.objects.all()  # Отримуємо всі теми
    return render(request, "topic_list.html", {"topics": topics})


# відображення списку редакторів
def redactor_list(request):
    redactors = Redactor.objects.all()  # Отримуємо всіх редакторів
    return render(request, "redactor_list.html", {"redactors": redactors})


# для створення нової газети
def newspaper_create(request):
    if request.method == "POST":
        form = NewspaperForm(request.POST)
        if form.is_valid():
            form.save()  # Зберігаємо нову газету
            return redirect("newspaper_list")  # Перенаправляємо на список газет
    else:
        form = NewspaperForm()
    return render(request, "newspaper_form.html", {"form": form})


# для редагування газети
def newspaper_edit(request, pk):
    newspaper = get_object_or_404(Newspaper, pk=pk)
    if request.method == "POST":
        form = NewspaperForm(request.POST, instance=newspaper)
        if form.is_valid():
            form.save()  # Оновлюємо газету
            return redirect("newspaper_list")  # Перенаправляємо на список газет
    else:
        form = NewspaperForm(instance=newspaper)
    return render(request, "newspaper_form.html", {"form": form})


# для створення нової теми
def topic_create(request):
    if request.method == "POST":
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("topic_list")  # Перенаправляємо на список тем
    else:
        form = TopicForm()
    return render(request, "topic_form.html", {"form": form})


# для редагування теми
def topic_edit(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    if request.method == "POST":
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            form.save()  # Оновлюємо тему
            return redirect("topic_list")  # Перенаправляємо на список тем
    else:
        form = TopicForm(instance=topic)
    return render(request, "topic_form.html", {"form": form})


# для створення нового редактора
def redactor_create(request):
    if request.method == "POST":
        form = RedactorForm(request.POST)
        if form.is_valid():
            form.save()  # Зберігаємо нового редактора
            return redirect("redactor_list")  # Перенаправляємо на список редакторів
    else:
        form = RedactorForm()
    return render(request, "redactor_form.html", {"form": form})


# для редагування редактора
def redactor_edit(request, pk):
    redactor = get_object_or_404(Redactor, pk=pk)
    if request.method == "POST":
        form = RedactorForm(request.POST, instance=redactor)
        if form.is_valid():
            form.save()  # Оновлюємо редактора
            return redirect("redactor_list")  # Перенаправляємо на список редакторів
    else:
        form = RedactorForm(instance=redactor)
    return render(request, "redactor_form.html", {"form": form})
