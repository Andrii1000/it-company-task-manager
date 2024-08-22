from django.test import TestCase

from catalog.forms import (
    TaskForm,
    WorkerForm,
    WorkerRegistrationForm,
    WorkerSearchForm,
    TaskSearchForm,
)
from catalog.models import (
    Worker,
    Task,
    Position,
    TaskType
)


class FormTestCase(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Developer")
        self.worker = Worker.objects.create_user(
            username="tester",
            email="test@ff.com",
            first_name="Test",
            last_name="User",
            position=self.position,
            password="1qwerty2",
        )
        self.task_type = TaskType.objects.create(name="Bug")
        self.task = Task.objects.create(
            name="Test Task",
            description="Test Description",
            deadline="2024-07-31",
            is_completed=False,
            priority="LOW",
            task_type=self.task_type,
        )


class TaskFormTest(FormTestCase):
    def test_task_form_valid(self):
        form_data = {
            "name": "Test Task",
            "description": "Test Description",
            "deadline": "2024-07-31",
            "is_completed": False,
            "priority": "LOW",
            "task_type": self.task_type,
            "assignees": [self.worker.id],
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_form_invalid(self):
        form_data = {}
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)


class WorkerFormTest(FormTestCase):
    def test_worker_form_valid(self):
        form_data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "first_name": "New",
            "last_name": "User",
            "position": self.position.id,
            "password1": "password123",
            "password2": "password123",
        }
        form = WorkerForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_worker_form_invalid(self):
        form_data = {}
        form = WorkerForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("username", form.errors)


class WorkerRegistrationFormTest(TestCase):
    def test_worker_registration_form_valid(self):
        form_data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "first_name": "New",
            "last_name": "User",
            "password": "password123",
            "confirm_password": "password123",
        }
        form = WorkerRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_worker_registration_form_invalid(self):
        form_data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "first_name": "New",
            "last_name": "User",
            "password": "password123",
            "confirm_password": "wrongpassword",
        }
        form = WorkerRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["__all__"], ["Passwords do not match"])


class WorkerSearchFormTest(TestCase):

    def test_worker_search_form(self):
        form_data = {"username": "testuser"}
        form = WorkerSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_worker_search_form_empty(self):
        form_data = {}
        form = WorkerSearchForm(data=form_data)
        self.assertTrue(form.is_valid())


class TaskSearchFormTest(TestCase):

    def test_task_search_form(self):
        form_data = {"name": "Test Task"}
        form = TaskSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_search_form_empty(self):
        form_data = {}
        form = TaskSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
