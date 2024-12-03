from django.urls import path
from . import views

urlpatterns = [
    path("newspapers/", views.newspaper_list, name="newspaper_list"),
    path("newspaper/<int:pk>/", views.newspaper_detail, name="newspaper_detail"),
    path("topics/", views.topic_list, name="topic_list"),
    path("redactors/", views.redactor_list, name="redactor_list"),
]
