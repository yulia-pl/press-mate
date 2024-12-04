from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib.auth import login
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import Newspaper, Topic, Redactor
from django.contrib import messages
from .forms import NewspaperForm, TopicForm, RedactorForm, RedactorRegistrationForm


# Домашня сторінка (загальнодоступна)
def home(request):
    return render(request, "home.html")


# Відображення списку газет (загальнодоступне)
def newspaper_list(request):
    topic_id = request.GET.get("topic")
    if topic_id:
        newspapers = Newspaper.objects.filter(topics__id=topic_id)
    else:
        newspapers = Newspaper.objects.all()

    # Перевірка, чи запит є AJAX
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        html = render_to_string("includes/newspaper_list_partial.html",
                                {"newspapers": newspapers})
        return JsonResponse({"html": html})

    topics = Topic.objects.all()
    return render(request, "newspaper_list.html",
                  {"newspapers": newspapers, "topics": topics})


# Відображення деталей газети (загальнодоступне)
def newspaper_detail(request, pk):
    newspaper = get_object_or_404(Newspaper, pk=pk)
    return render(request, "newspaper_detail.html", {"newspaper": newspaper})


# Відображення списку тем (загальнодоступне)
def topic_list(request):
    topics = Topic.objects.all()
    return render(request, "topic_list.html", {"topics": topics})


# Відображення списку редакторів (лише для авторизованих користувачів)
@login_required
def redactor_list(request):
    redactors = Redactor.objects.all()
    return render(request, "redactor_list.html", {"redactors": redactors})


# Редагування газети (лише для авторизованих користувачів)
@login_required
def newspaper_edit(request, pk):
    newspaper = get_object_or_404(Newspaper, pk=pk)
    if request.method == "POST":
        form = NewspaperForm(request.POST, instance=newspaper)
        if form.is_valid():
            form.save()
            return redirect("newspaper_list")
    else:
        form = NewspaperForm(instance=newspaper)
    return render(request, "newspaper_form.html", {"form": form})


# Створення нової теми (лише для авторизованих користувачів)
@login_required
def topic_create(request):
    if request.method == "POST":
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("topic_list")
    else:
        form = TopicForm()
    return render(request, "topic_form.html", {"form": form})


# Редагування теми (лише для авторизованих користувачів)
@login_required
def topic_edit(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    if request.method == "POST":
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            form.save()
            return redirect("topic_list")
    else:
        form = TopicForm(instance=topic)
    return render(request, "topic_form.html", {"form": form})


# Реєстрація нового користувача (загальнодоступна)
def register(request):
    if request.method == "POST":
        form = RedactorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            # Надсилання email
            current_site = get_current_site(request)
            subject = "Activate Your Account"
            message = render_to_string("activation_email.html", {
                "user": user,
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": default_token_generator.make_token(user),
            })
            send_mail(subject, message, "noreply@yourdomain.com", [user.email])

            messages.success(request, "Registration successful. "
                                      "If you are an admin, you can access "
                                      "the admin panel after activation.")
            return render(request, "registration_complete.html")
    else:
        form = RedactorRegistrationForm()
    return render(request, "register.html", {"form": form})


# Активація облікового запису через email (загальнодоступна)
def activate_account(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Redactor.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Redactor.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return render(request, "activation_successful.html")
    else:
        return render(request, "activation_invalid.html")


# Профіль користувача (лише для авторизованих користувачів)
@login_required
def profile(request):
    return render(request, "profile.html")


# Створення нового редактора (лише для авторизованих користувачів)
@login_required
def redactor_create(request):
    if request.method == "POST":
        form = RedactorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("redactor_list")
    else:
        form = RedactorForm()
    return render(request, "redactor_form.html", {"form": form})


# Редагування редактора (лише для авторизованих користувачів)
@login_required
def redactor_edit(request, pk):
    redactor = get_object_or_404(Redactor, pk=pk)
    if request.method == "POST":
        form = RedactorForm(request.POST, instance=redactor)
        if form.is_valid():
            form.save()
            return redirect("redactor_list")
    else:
        form = RedactorForm(instance=redactor)
    return render(request, "redactor_form.html",
                  {"form": form, "redactor": redactor})


def latest_news(request):
    latest_newspapers = Newspaper.objects.order_by("-published_date")[:5]
    data = [
        {
            "title": newspaper.title,
            "id": newspaper.id,
            "published_date": newspaper.published_date.strftime("%Y-%m-%d")
        }
        for newspaper in latest_newspapers
    ]
    return JsonResponse(data, safe=False)
