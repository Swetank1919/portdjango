from django.contrib import admin
from .models import Project,Skill,Message

# Register your models here.
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Message)