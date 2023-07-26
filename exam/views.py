from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.urls import reverse_lazy

from .models import Task, Tag
from .forms import TaskCreateForm, TagForm


class TaskListView(generic.ListView):
    model = Task
    template_name = "exam/task_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = "exam/task_form.html"
    success_url = reverse_lazy("exam:home")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskCreateForm
    template_name = "exam/task_form.html"
    success_url = reverse_lazy("exam:home")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "exam/task_delete_warning.html"
    success_url = reverse_lazy("exam:home")


def complete_uncomplete_task(request, pk):
    task = Task.objects.get(id=pk)
    if task.is_done:
        task.is_done = False
    else:
        task.is_done = True
    task.save()
    return HttpResponseRedirect(reverse_lazy("exam:home"))


class TagListView(generic.ListView):
    model = Tag
    template_name = "exam/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("exam:tags-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("exam:tags-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "exam/tag_delete_warning.html"
    success_url = reverse_lazy("exam:tags-list")
