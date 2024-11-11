from django.urls import path
from . import views

app_name = 'app_name'

urlpatterns = [
    path('employees/', views.EmployeeListView, name='employee_list'),
    path('employees/create/', views.EmployeeCreateView, name='employee_create'),
    path('employees/<int:pk>/', views.EmployeeDetailView, name='employee_detail'),
    path('employees/<int:pk>/update/', views.EmployeeUpdateView, name='employee_update'),
    path('employees/<int:pk>/delete/', views.EmployeeDeleteView, name='employee_delete'),

    path('departments/', views.DepartmentListView, name='department_list'),
    path('departments/create/', views.DepartmentCreateView, name='department_create'),
    path('departments/<int:pk>/', views.DepartmentDetailView, name='department_detail'),
    path('departments/<int:pk>/update/', views.DepartmentUpdateView, name='department_update'),
    path('departments/<int:pk>/delete/', views.DepartmentDeleteView, name='department_delete'),

    path('feedbacks/', views.FeedbackListView, name='feedback_list'),
    path('feedbacks/create/', views.FeedbackCreateView, name='feedback_create'),
    path('feedbacks/<int:pk>/', views.FeedbackDetailView, name='feedback_detail'),
    path('feedbacks/<int:pk>/update/', views.FeedbackUpdateView, name='feedback_update'),
    path('feedbacks/<int:pk>/delete/', views.FeedbackDeleteView, name='feedback_delete'),

    path('conflicts/', views.ConflictResolutionListView, name='conflict_list'),
    path('conflicts/create/', views.ConflictResolutionCreateView, name='conflict_create'),
    path('conflicts/<int:pk>/', views.ConflictResolutionDetailView, name='conflict_detail'),
    path('conflicts/<int:pk>/update/', views.ConflictResolutionUpdateView, name='conflict_update'),
    path('conflicts/<int:pk>/delete/', views.ConflictResolutionDeleteView, name='conflict_delete'),
]