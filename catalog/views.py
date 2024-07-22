from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic


from catalog.forms import WorkerForm, TaskForm, WorkerRegistrationForm, WorkerSearchForm, TaskSearchForm
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
    queryset = Worker.objects.select_related("position")
    context_object_name = "workers"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = WorkerSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        form = WorkerSearchForm(self.request.GET)
        if form.is_valid():
            return self.queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return self.queryset


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    context_object_name = "worker"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        worker = self.object
        context['completed_tasks'] = Task.objects.filter(assignees=worker, is_completed=True)
        context['not_completed_tasks'] = Task.objects.filter(assignees=worker, is_completed=False)
        return context


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
    paginate_by = 6
    context_object_name = "tasks"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        task_type = self.request.GET.get("task_type", "")
        context["search_form"] = TaskSearchForm(
            initial={"task_type": task_type}
        )
        return context

    def get_queryset(self):
        queryset = Task.objects.all()
        form = TaskSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


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


def custom_logout_view(request):
    logout(request)
    return redirect('login')


def register_worker(request):
    if request.method == 'POST':
        form = WorkerRegistrationForm(request.POST)
        if form.is_valid():
            worker = form.save(commit=False)
            worker.set_password(form.cleaned_data['password'])
            worker.save()
            return redirect('login')
    else:
        form = WorkerRegistrationForm()
    return render(request, 'accounts/sign-up.html', {'form': form})
