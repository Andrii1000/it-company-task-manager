from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic


from catalog.forms import WorkerForm, TaskForm
from catalog.models import Worker, Task, Position


@login_required
def index(request):
    num_workers = Worker.objects.count()
    num_tasks = Task.objects.count()
    num_positions = Position.objects.count()

    context = {
        "num_workers": num_workers,
        "num_tasks": num_tasks,
        "num_positions": num_positions,
    }

    return render(request, "catalog/index.html", context=context)


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    paginate_by = 10
    context_object_name = "workers"


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker


class WorkerCreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Worker
    success_url = reverse_lazy('catalog:worker-list')
    form_class = WorkerForm


class WorkerUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Worker
    success_url = reverse_lazy('catalog:worker-list')
    form_class = WorkerForm


class WorkerDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Worker
    success_url = reverse_lazy("catalog:worker-list")


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    queryset = Task.objects.select_related("task_type").prefetch_related("assignees")
    ordering = ["deadline"]
    paginate_by = 4
    context_object_name = "tasks"


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    context_object_name = "task"


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("catalog:task-list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Task
    success_url = reverse_lazy("catalog:task-list")
    form_class = TaskForm


class TaskDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Task
    success_url = reverse_lazy("catalog:task-list")




