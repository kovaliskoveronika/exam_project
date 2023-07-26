from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=150)


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(null=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")
