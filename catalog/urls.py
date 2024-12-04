from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("home/", views.home, name="home"),
    path("newspapers/", views.newspaper_list, name="newspaper_list"),
    path("newspaper/<int:pk>/", views.newspaper_detail, name="newspaper_detail"),
    path("newspaper/<int:pk>/edit/", views.newspaper_edit, name="newspaper_edit"),
    path("topics/", views.topic_list, name="topic_list"),
    path("topic/create/", views.topic_create, name="topic_create"),
    path("topic/<int:pk>/edit/", views.topic_edit, name="topic_edit"),
    path("redactors/", views.redactor_list, name="redactor_list"),
    path("redactor/create/", views.redactor_create, name="redactor_create"),
    path("redactor/<int:pk>/edit/", views.redactor_edit, name="redactor_edit"),
    path("register/", views.register, name="register"),
    path("activate/<uidb64>/<token>/", views.activate_account,
         name="activate_account"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"),
         name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="logout.html"),
         name="logout"),
    path("profile/", views.profile, name="profile"),
    path("api/latest-news/", views.latest_news, name="latest_news"),
]

# Додатково додаємо обробку медіафайлів, якщо DEBUG=True
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
