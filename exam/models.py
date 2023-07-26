from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    create_date = models.DateTimeField(default=timezone.now, null=True)
    deadline = models.DateTimeField(null=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")
