from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Newspaper, Topic, Redactor

class NewspaperTests(TestCase):
    def setUp(self):
        # Створення тестового користувача
        self.user = User.objects.create_user(username="testuser", password="testpassword123")
        self.topic = Topic.objects.create(name="Politics")
        self.newspaper = Newspaper.objects.create(
            title="Test Newspaper", content="Test Content", published_date="2024-12-01"
        )
        self.newspaper.topics.add(self.topic)

    def test_newspaper_create_view(self):
        self.client.login(username="testuser", password="testpassword123")
        response = self.client.post(reverse("newspaper_create"), {
            "title": "New Test Newspaper",
            "content": "Content of the new newspaper",
            "published_date": "2024-12-02"
        })
        self.assertEqual(response.status_code, 302)  # Перенаправлення на список газет
        self.assertRedirects(response, reverse("newspaper_list"))

    def test_newspaper_edit_view(self):
        self.client.login(username="testuser", password="testpassword123")
        response = self.client.post(reverse("newspaper_edit", args=[self.newspaper.pk]), {
            "title": "Updated Test Newspaper",
            "content": "Updated content of the newspaper",
            "published_date": "2024-12-03"
        })
        self.assertEqual(response.status_code, 302)  # Перенаправлення на список газет
        self.assertRedirects(response, reverse("newspaper_list"))
        self.newspaper.refresh_from_db()
        self.assertEqual(self.newspaper.title, "Updated Test Newspaper")

class RedactorTests(TestCase):
    def setUp(self):
        # Створення тестового користувача
        self.user = User.objects.create_user(username="testuser", password="testpassword123")
        self.redactor = Redactor.objects.create_user(
            username="editor1",
            email="editor1@example.com",
            password="testpassword123",
            years_of_experience=3
        )

    def test_redactor_create_view(self):
        self.client.login(username="testuser", password="testpassword123")
        response = self.client.post(reverse("redactor_create"), {
            "username": "new_editor",
            "email": "new_editor@example.com",
            "years_of_experience": 5
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("redactor_list"))

    def test_redactor_edit_view(self):
        self.client.login(username="testuser", password="testpassword123")
        response = self.client.post(reverse("redactor_edit", args=[self.redactor.pk]), {
            "username": "updated_editor",
            "email": "updated_editor@example.com",
            "years_of_experience": 5
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("redactor_list"))
        self.redactor.refresh_from_db()
        self.assertEqual(self.redactor.username, "updated_editor")

class TopicTests(TestCase):
    def setUp(self):
        # Створення тестового користувача та теми
        self.user = User.objects.create_user(username="testuser", password="testpassword123")
        self.topic = Topic.objects.create(name="Technology")

    def test_topic_create_view(self):
        self.client.login(username="testuser", password="testpassword123")
        response = self.client.post(reverse("topic_create"), {
            "name": "New Topic"
        })
        self.assertEqual(response.status_code, 302)  # Перенаправлення на список тем
        self.assertRedirects(response, reverse("topic_list"))

    def test_topic_edit_view(self):
        self.client.login(username="testuser", password="testpassword123")
        response = self.client.post(reverse("topic_edit", args=[self.topic.pk]), {
            "name": "Updated Topic"
        })
        self.assertEqual(response.status_code, 302)  # Перенаправлення на список тем
        self.assertRedirects(response, reverse("topic_list"))
        self.topic.refresh_from_db()
        self.assertEqual(self.topic.name, "Updated Topic")
