from django.urls import path
from . import views

urlpatterns = [
    path('', views.find_item, name='find_item'),
]