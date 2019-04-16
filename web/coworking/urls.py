from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='coworking_index'),
]
