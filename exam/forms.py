import datetime

from django import forms
from django.core.exceptions import ValidationError

from .models import Task, Tag


class TaskCreateForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = ["content", "create_date", "deadline", "tags"]
        widgets = {
            "create_date": forms.DateInput(attrs={"type": "date"}),
            "deadline": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["deadline"].required = False


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
