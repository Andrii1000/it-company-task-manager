# test_views.py
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from catalog.models import (
    Worker,
    Task,
    Position,
    TaskType
)


User = get_user_model()

class IndexViewTest(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse("catalog:index"))
        self.assertEqual(
            response.status_code, 302
        )  # Should redirect to login if not authenticated
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("catalog:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/index.html")


class ViewsTestCase(TestCase):
    def setUp(self):
        self.task_type = TaskType.objects.create(name="Bug")
        self.position = Position.objects.create(name="Developer")
        self.worker = Worker.objects.create_user(
            username="testuser",
            email="test@example.com",
            first_name="Test",
            last_name="User",
            position=self.position,
            password="testpassword",
        )
        self.task = Task.objects.create(
            name="Test Task",
            description="Test Description",
            deadline="2024-07-31",
            is_completed=False,
            priority="HIGH",
            task_type=self.task_type,
        )
        self.task.assignees.add(self.worker)


class WorkerListViewTest(ViewsTestCase):
    def test_worker_list_view(self):
        response = self.client.get(reverse("catalog:worker-list"))
        self.assertEqual(
            response.status_code, 302
        )  # Should redirect to login if not authenticated
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("catalog:worker-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/worker_list.html")


class WorkerDetailViewTest(ViewsTestCase):
    def test_worker_detail_view(self):
        response = self.client.get(
            reverse("catalog:worker-detail", kwargs={"pk": self.worker.pk})
        )
        self.assertEqual(
            response.status_code, 302
        )  # Should redirect to login if not authenticated
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(
            reverse("catalog:worker-detail", kwargs={"pk": self.worker.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/worker_detail.html")


class WorkerCreateViewTest(ViewsTestCase):
    def test_worker_create_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("catalog:worker-create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/worker_form.html")


class WorkerUpdateViewTest(ViewsTestCase):
    def test_worker_update_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(
            reverse("catalog:worker-update", kwargs={"pk": self.worker.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/worker_form.html")


class WorkerDeleteViewTest(ViewsTestCase):
    def test_worker_delete_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(
            reverse("catalog:worker-delete", kwargs={"pk": self.worker.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/worker_confirm_delete.html")


class TaskListViewTest(ViewsTestCase):
    def test_task_list_view(self):
        response = self.client.get(reverse("catalog:task-list"))
        self.assertEqual(
            response.status_code, 302
        )  # Should redirect to login if not authenticated
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("catalog:task-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/task_list.html")


class TaskDetailViewTest(ViewsTestCase):
    def test_task_detail_view(self):
        response = self.client.get(
            reverse("catalog:task-detail", kwargs={"pk": self.task.pk})
        )
        self.assertEqual(
            response.status_code, 302
        )  # Should redirect to login if not authenticated
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(
            reverse("catalog:task-detail", kwargs={"pk": self.task.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/task_detail.html")


class TaskCreateViewTest(ViewsTestCase):
    def test_task_create_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("catalog:task-create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/task_form.html")


class TaskUpdateViewTest(ViewsTestCase):
    def test_task_update_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(
            reverse("catalog:task-update", kwargs={"pk": self.task.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/task_form.html")


class TaskDeleteViewTest(ViewsTestCase):
    def test_task_delete_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(
            reverse("catalog:task-delete", kwargs={"pk": self.task.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/task_confirm_delete.html")
