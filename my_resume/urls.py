from django.urls import path
from my_resume import views

urlpatterns = [
    path('',views.home,name='home'),
    path('toggle_mode/',views.toggle_mode,name='toggle_mode'),
]