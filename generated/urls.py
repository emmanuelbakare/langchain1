from django.urls import path
from . import views

app_name = 'your_app_name'

urlpatterns = [
    path('employees/', views.EmployeeListView.as_view(), name='employee_list'),
    path('employees/create/', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('employees/<int:pk>/update/', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('employees/<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee_delete'),
    path('departments/', views.DepartmentListView.as_view(), name='department_list'),
    path('departments/create/', views.DepartmentCreateView.as_view(), name='department_create'),
    path('departments/<int:pk>/update/', views.DepartmentUpdateView.as_view(), name='department_update'),
    path('departments/<int:pk>/delete/', views.DepartmentDeleteView.as_view(), name='department_delete'),
    path('feedbacks/', views.FeedbackListView.as_view(), name='feedback_list'),
    path('feedbacks/create/', views.FeedbackCreateView.as_view(), name='feedback_create'),
    path('feedbacks/<int:pk>/update/', views.FeedbackUpdateView.as_view(), name='feedback_update'),
    path('feedbacks/<int:pk>/delete/', views.FeedbackDeleteView.as_view(), name='feedback_delete'),
    path('meetings/', views.MeetingListView.as_view(), name='meeting_list'),
    path('meetings/create/', views.MeetingCreateView.as_view(), name='meeting_create'),
    path('meetings/<int:pk>/update/', views.MeetingUpdateView.as_view(), name='meeting_update'),
    path('meetings/<int:pk>/delete/', views.MeetingDeleteView.as_view(), name='meeting_delete'),
]