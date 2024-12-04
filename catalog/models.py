from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


# Модель для тем газети
class Topic(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Назва теми

    def __str__(self):
        return self.name


# Модель для користувачів (редакторів)
class Redactor(AbstractUser):
    years_of_experience = models.PositiveIntegerField(default=0)  # Досвід у роках

    groups = models.ManyToManyField(
        Group,
        related_name="redactor_set",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="redactor_set",
        blank=True
    )

    def __str__(self):
        return f"{self.username} ({self.years_of_experience} років досвіду)"


# Модель для газет
class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateField()
    topics = models.ManyToManyField("Topic", related_name="newspapers")
    redactors = models.ManyToManyField("Redactor", related_name="newspapers")
    image = models.ImageField(upload_to="newspapers/", blank=True, null=True)
