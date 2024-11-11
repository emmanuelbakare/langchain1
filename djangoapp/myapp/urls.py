from django.urls import path 
from . import views
urlpatterns = [
    path('', views.test, name="tester"),
    path('contacts', views.contacts, name="contact-list"),
    path('add-contact', views.add_contact, name="add-contact"),
]
