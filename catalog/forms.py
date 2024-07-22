from django import forms
from django.contrib.auth.forms import UserCreationForm

from catalog.models import Worker, Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'name',
            'description',
            'deadline',
            'is_completed',
            'priority',
            'task_type',
            'assignees'
        ]
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
            'assignees': forms.CheckboxSelectMultiple(),
        }


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
            "position",
        )


class WorkerRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = Worker
        fields = (
            'position',
            'username',
            'email',
            'first_name',
            'last_name'
        )
        labels = {
            'position': 'Position',
            'username': 'Username',
            'email': 'Email',
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data


class WorkerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=120,
        required=False,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Search by Username'}),
    )


class TaskSearchForm(forms.Form):
    name = forms.CharField(
        max_length=120,
        required=False,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Search by name'})
    )
