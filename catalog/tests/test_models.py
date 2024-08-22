# test_models.py
from django.test import TestCase
from django.contrib.auth import get_user_model

from catalog.models import (
    TaskType,
    Position,
    Task
)


User = get_user_model()

class ModelTestCase(TestCase):
    def setUp(self):
        # Common setup for all tests
        self.position = Position.objects.create(name="Developer")
        self.worker = User.objects.create_user(
            username="testuser",
            password="testpassword",
            first_name="Test",
            last_name="User",
            position=self.position,
        )
        self.task_type = TaskType.objects.create(name="Bug Fix")
        self.task = Task.objects.create(
            name="Test Task",
            description="Test Description",
            deadline="2024-07-31",
            is_completed=False,
            priority="High",
            task_type=self.task_type,
        )
        self.task.assignees.add(self.worker)

    def test_task_type_str(self):
        self.assertEqual(str(self.task_type), "Bug Fix")

    def test_task_assignees(self):
        self.assertEqual(self.task.assignees.count(), 1)
        self.assertEqual(self.task.assignees.first(), self.worker)

    def test_position_str(self):
        self.assertEqual(str(self.position), "Developer")

    def test_worker_str(self):
        self.assertEqual(str(self.worker), "testuser (Test User)")

    def test_task_ordering(self):
        task2 = Task.objects.create(
            name="Test Task 2",
            description="Test Description 2",
            deadline="2024-07-30",
            is_completed=False,
            priority="High",
            task_type=self.task_type,
        )
        tasks = Task.objects.all()
        self.assertEqual(tasks[0], task2)
        self.assertEqual(tasks[1], self.task)
