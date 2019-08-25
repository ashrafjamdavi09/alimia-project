from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminHome, name='adminHome'),
    path('regisrations', views.regisrations, name='regisrations'),
]
