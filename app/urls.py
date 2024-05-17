from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('projects/',views.project,name='project'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('skill',views.skill,name='skill'),
    path('dskill/<int:id>',views.dskill,name='dskill'),
    path('contact/',views.contact,name='contact'),
    
]
