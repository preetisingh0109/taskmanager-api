from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from .models import Task


class TaskAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user("preeti", password="pass12345")
        self.other = User.objects.create_user("other", password="pass12345")
        self.client.force_authenticate(self.user)

    def test_create_task(self):
        res = self.client.post("/api/tasks/", {"title": "Write README"})
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.data["owner"], "preeti")

    def test_user_sees_only_own_tasks(self):
        Task.objects.create(owner=self.other, title="Not yours")
        Task.objects.create(owner=self.user, title="Mine")
        res = self.client.get("/api/tasks/")
        self.assertEqual(res.data["count"], 1)

    def test_cannot_access_other_users_task(self):
        t = Task.objects.create(owner=self.other, title="Secret")
        self.assertEqual(self.client.get(f"/api/tasks/{t.id}/").status_code, 404)

    def test_complete_action(self):
        t = Task.objects.create(owner=self.user, title="Ship it")
        res = self.client.post(f"/api/tasks/{t.id}/complete/")
        self.assertEqual(res.data["status"], "done")

    def test_requires_auth(self):
        self.client.force_authenticate(None)
        self.assertEqual(self.client.get("/api/tasks/").status_code, 401)
