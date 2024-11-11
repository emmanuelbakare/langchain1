from django.urls import path
from .views import ContactCreateView, ContactListView, ContactDetailView

urlpatterns = [
    path('contacts/', ContactListView.as_view(), name='contact_list'),
    path('contacts/new/', ContactCreateView.as_view(), name='contact_create'),
    path('contacts/<int:pk>/', ContactDetailView.as_view(), name='contact_detail'),
]