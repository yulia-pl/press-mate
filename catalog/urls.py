from django.urls import path
from . import views

urlpatterns = [
    path("newspapers/", views.newspaper_list, name="newspaper_list"),
    path("newspaper/<int:pk>/", views.newspaper_detail, name="newspaper_detail"),
    path("newspaper/create/", views.newspaper_create, name="newspaper_create"),
    path("newspaper/<int:pk>/edit/", views.newspaper_edit, name="newspaper_edit"),
    path("topics/", views.topic_list, name="topic_list"),
    path("topic/create/", views.topic_create, name="topic_create"),
    path("topic/<int:pk>/edit/", views.topic_edit, name="topic_edit"),
    path("redactors/", views.redactor_list, name="redactor_list"),
    path("redactor/create/", views.redactor_create, name="redactor_create"),
    path("redactor/<int:pk>/edit/", views.redactor_edit, name="redactor_edit"),
]
