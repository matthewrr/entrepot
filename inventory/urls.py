from django.urls import path
from .views import *

urlpatterns = [
    path('', ItemListView.as_view(), name='view_items'),
    path('item/list/', ItemListView.as_view(), name="item_list"),
    path('item/create/', ItemCreateView.as_view(), name="item_create"),
    path('item/<int:pk>/', ItemDetailView.as_view(), name="item_detail"),
    path('item/<int:pk>/update/', ItemUpdateView.as_view(), name="item_update"),
    path('item/<int:pk>/delete/', ItemDeleteView.as_view(), name="item_delete"),
    path('ajax/item_categories/', item_categories, name='item_categories'),
]