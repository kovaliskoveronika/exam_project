from django.urls import path

from .views import TaskListView, TaskCreateView, complete_uncomplete_task, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("task/", TaskCreateView.as_view(), name="task-create"),
    path("task/complete/<int:pk>/", complete_uncomplete_task, name="task-complete"),
    path("task/<int:pk>", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete", TaskDeleteView.as_view(), name="task-delete")
]

app_name = "exam"
