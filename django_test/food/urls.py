from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    # List all items
    path('', views.item_list, name='item_list'),
    
    # Create a new item
    path('new/', views.item_create, name='item_create'),
    
    # Retrieve a specific item
    path('<int:pk>/', views.item_detail, name='item_detail'),
    
    # Update an existing item
    path('<int:pk>/edit/', views.item_update, name='item_update'),
    
    # Delete an item
    path('<int:pk>/delete/', views.item_delete, name='item_delete'),

    #fake Data
    path('fake/<int:total>/', views.fake_item, name='fake_item'),
]