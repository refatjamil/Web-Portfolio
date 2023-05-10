from django.urls import path
from . import views

urlpatterns = [
    path('',views.project,name='project'),
    path('toggle_mode/',views.toggle_mode,name='toggle_mode'),

]