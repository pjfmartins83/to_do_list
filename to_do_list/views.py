from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

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
