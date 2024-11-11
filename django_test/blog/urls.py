from django.urls import path
from . import views

app_name = 'blog'  # This sets the application namespace

urlpatterns = [
    # List view for all blog posts
    path('', views.post_list, name='post_list'),
    
    # Detail view for a single blog post
    path('<int:pk>/', views.post_detail, name='post_detail'),
    
    # Create view for a new blog post
    path('new/', views.post_create, name='post_create'),
    
    # Update view for an existing blog post
    path('<int:pk>/edit/', views.post_update, name='post_update'),
    
    # Delete view for a blog post
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),

    #generate fake data
    path('fake/<int:total>', views.fake_post, name='fake_posts')
]

# This urls.py file defines the URL patterns for the blog application.
# Each path corresponds to a view function in views.py.
# The 'name' parameter allows for easy URL reversing in templates and views.
# The 'app_name' variable sets the application namespace, allowing for
# differentiation between URL names in different apps.