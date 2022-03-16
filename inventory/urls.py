from django.urls import path
from . import views

urlpatterns = [
    # path('', views.find_item, name='find_item'),
    path('', views.view_items, name='view_items'),
    path('item/add/', views.add_item, name='item_add'),
    path('item/categories/', views.item_categories, name='item_categories'),
    path('ajax/item_categories/', views.item_categories, name='item_categories'),
]