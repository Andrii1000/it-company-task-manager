# test_models.py
from django.test import TestCase
from django.contrib.auth import get_user_model
from catalog.models import (
    TaskType,
    Position,
    Worker,
    Task
)
from django.urls import reverse

User = get_user_model()


class TaskTypeModelTest(TestCase):

    def setUp(self):
        self.task_type = TaskType.objects.create(name="Bug")

    def test_task_type_str(self):
        self.assertEqual(str(self.task_type), self.task_type.name)


class PositionModelTest(TestCase):

    def setUp(self):
        self.position = Position.objects.create(name="Developer")

    def test_position_str(self):
        self.assertEqual(str(self.position), self.position.name)


class WorkerModelTest(TestCase):

    def setUp(self):
        self.position = Position.objects.create(name="Developer")
        self.worker = Worker.objects.create_user(
            username='testuser',
            email='test@example.com',
            first_name='Test',
            last_name='User',
            position=self.position,
            password='testpassword'
        )

    def test_worker_str(self):
        self.assertEqual(str(self.worker), f"{self.worker.username} ({self.worker.first_name} {self.worker.last_name})")

    def test_get_absolute_url(self):
        url = self.worker.get_absolute_url()
        expected_url = reverse("catalog:worker-detail", kwargs={"pk": self.worker.pk})
        self.assertEqual(url, expected_url)


class TaskModelTest(TestCase):

    def setUp(self):
        self.task_type = TaskType.objects.create(name="Bug")
        self.position = Position.objects.create(name="Developer")
        self.worker = Worker.objects.create_user(
            username='testuser',
            email='test@example.com',
            first_name='Test',
            last_name='User',
            position=self.position,
            password='testpassword'
        )
        self.task = Task.objects.create(
            name='Test Task',
            description='Test Description',
            deadline='2024-07-31',
            is_completed=False,
            priority='High',
            task_type=self.task_type
        )
        self.task.assignees.add(self.worker)

    def test_task_str(self):
        self.assertEqual(str(self.task), self.task.name)

    def test_task_assignees(self):
        self.assertEqual(self.task.assignees.count(), 1)
        self.assertEqual(self.task.assignees.first(), self.worker)

    def test_task_ordering(self):
        task2 = Task.objects.create(
            name='Test Task 2',
            description='Test Description 2',
            deadline='2024-07-30',
            is_completed=False,
            priority='High',
            task_type=self.task_type
        )
        tasks = Task.objects.all()
        self.assertEqual(tasks[0], task2)
        self.assertEqual(tasks[1], self.task)
