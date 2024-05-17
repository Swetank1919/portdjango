from typing import Any, Mapping
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.utils import ErrorList
from .models import Project,Skill
from django import forms
from django.forms.utils import ErrorList
class Projectform(ModelForm):
    class Meta:
        model=Project
        fields='__all__'
class Skillform(ModelForm):
    class Meta:
        model=Skill
        fields='__all__'

   