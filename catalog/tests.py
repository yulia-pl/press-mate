from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Newspaper, Topic, Redactor


class NewspaperTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser",
                                             password="testpassword123")
        self.client.login(username="testuser", password="testpassword123")

        self.topic = Topic.objects.create(name="Politics")
        self.redactor = Redactor.objects.create_user(
            username="editor1",
            email="editor1@example.com",
            password="testpassword123",
            years_of_experience=5
        )

        self.newspaper = Newspaper.objects.create(
            title="Test Newspaper",
            content="Test Content",
            published_date="2024-12-01"
        )
        self.newspaper.topics.add(self.topic)
        self.newspaper.redactors.add(self.redactor)

    def test_newspaper_list_view(self):
        response = self.client.get(reverse("newspaper_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Newspaper")

    def test_newspaper_detail_view(self):
        response = self.client.get(reverse("newspaper_detail",
                                           args=[self.newspaper.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Content")

    def test_newspaper_edit_view(self):
        response = self.client.post(reverse("newspaper_edit",
                                            args=[self.newspaper.pk]), {
            "title": "Updated Test Newspaper",
            "content": "Updated content of the newspaper",
            "published_date": "2024-12-03",
            "topics": [self.topic.pk],
            "redactors": [self.redactor.pk]
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("newspaper_list"))
        self.newspaper.refresh_from_db()
        self.assertEqual(self.newspaper.title, "Updated Test Newspaper")
        self.assertEqual(self.newspaper.content, "Updated content of the newspaper")


class TopicTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser",
                                             password="testpassword123")
        self.client.login(username="testuser", password="testpassword123")
        self.topic = Topic.objects.create(name="Technology")

    def test_topic_list_view(self):
        response = self.client.get(reverse("topic_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Technology")

    def test_topic_create_view(self):
        response = self.client.post(reverse("topic_create"), {
            "name": "New Topic"
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("topic_list"))
        self.assertTrue(Topic.objects.filter(name="New Topic").exists())

    def test_topic_edit_view(self):
        response = self.client.post(reverse("topic_edit", args=[self.topic.pk]), {
            "name": "Updated Topic"
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("topic_list"))
        self.topic.refresh_from_db()
        self.assertEqual(self.topic.name, "Updated Topic")


class RedactorTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser",
                                             password="testpassword123")
        self.client.login(username="testuser", password="testpassword123")
        self.redactor = Redactor.objects.create_user(
            username="editor1",
            email="editor1@example.com",
            password="testpassword123",
            years_of_experience=5
        )

    def test_redactor_list_view(self):
        response = self.client.get(reverse("redactor_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "editor1")

    def test_redactor_create_view(self):
        response = self.client.post(reverse("redactor_create"), {
            "username": "new_editor",
            "email": "new_editor@example.com",
            "years_of_experience": 5,
            "password": "testpassword123",
            "password_confirmation": "testpassword123"
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("redactor_list"))
        self.assertTrue(Redactor.objects.filter(username="new_editor").exists())

    def test_redactor_edit_view(self):
        response = self.client.post(reverse("redactor_edit",
                                            args=[self.redactor.pk]), {
            "username": "updated_editor",
            "email": "updated_editor@example.com",
            "years_of_experience": 6
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("redactor_list"))
        self.redactor.refresh_from_db()
        self.assertEqual(self.redactor.username, "updated_editor")
        self.assertEqual(self.redactor.years_of_experience, 6)
