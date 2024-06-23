from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Task


class TaskListView(ListView):
    model = Task
    template_name = "home.html"


class TaskDetailView(DetailView):
    model = Task
    template_name = "task_detail.html"


class TaskCreateView(CreateView):
    model = Task
    template_name = "task_new.html"
    fields = ["title", "author", "body"]


class TaskUpdateView(UpdateView):
    model = Task
    template_name = "task_edit.html"
    fields = ["title", "body"]


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "task_delete.html"
    success_url = reverse_lazy("home")
