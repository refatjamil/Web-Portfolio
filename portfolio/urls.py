from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('project/',views.project,name='project'),
    path('skill',views.skill,name='skill'),

    path('toggle_mode/',views.toggle_mode,name='toggle_mode'),
]