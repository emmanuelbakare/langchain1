from django.urls import path
from . import views

urlpatterns = [
    # Employee URLs
    path('employees/', views.EmployeeListView.as_view(), name='employee_list'),
    path('employees/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('employees/create/', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('employees/<int:pk>/update/', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('employees/<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee_delete'),

    # Department URLs
    path('departments/', views.DepartmentListView.as_view(), name='department_list'),
    path('departments/<int:pk>/', views.DepartmentDetailView.as_view(), name='department_detail'),
    path('departments/create/', views.DepartmentCreateView.as_view(), name='department_create'),
    path('departments/<int:pk>/update/', views.DepartmentUpdateView.as_view(), name='department_update'),
    path('departments/<int:pk>/delete/', views.DepartmentDeleteView.as_view(), name='department_delete'),

    # Position URLs
    path('positions/', views.PositionListView.as_view(), name='position_list'),
    path('positions/<int:pk>/', views.PositionDetailView.as_view(), name='position_detail'),
    path('positions/create/', views.PositionCreateView.as_view(), name='position_create'),
    path('positions/<int:pk>/update/', views.PositionUpdateView.as_view(), name='position_update'),
    path('positions/<int:pk>/delete/', views.PositionDeleteView.as_view(), name='position_delete'),

    # EmployeeRelation URLs
    path('employee-relations/', views.EmployeeRelationListView.as_view(), name='employee_relation_list'),
    path('employee-relations/<int:pk>/', views.EmployeeRelationDetailView.as_view(), name='employee_relation_detail'),
    path('employee-relations/create/', views.EmployeeRelationCreateView.as_view(), name='employee_relation_create'),
    path('employee-relations/<int:pk>/update/', views.EmployeeRelationUpdateView.as_view(), name='employee_relation_update'),
    path('employee-relations/<int:pk>/delete/', views.EmployeeRelationDeleteView.as_view(), name='employee_relation_delete'),

    # Feedback URLs
    path('feedbacks/', views.FeedbackListView.as_view(), name='feedback_list'),
    path('feedbacks/<int:pk>/', views.FeedbackDetailView.as_view(), name='feedback_detail'),
    path('feedbacks/create/', views.FeedbackCreateView.as_view(), name='feedback_create'),
    path('feedbacks/<int:pk>/update/', views.FeedbackUpdateView.as_view(), name='feedback_update'),
    path('feedbacks/<int:pk>/delete/', views.FeedbackDeleteView.as_view(), name='feedback_delete'),

    # Meeting URLs
    path('meetings/', views.MeetingListView.as_view(), name='meeting_list'),
    path('meetings/<int:pk>/', views.MeetingDetailView.as_view(), name='meeting_detail'),
    path('meetings/create/', views.MeetingCreateView.as_view(), name='meeting_create'),
    path('meetings/<int:pk>/update/', views.MeetingUpdateView.as_view(), name='meeting_update'),
    path('meetings/<int:pk>/delete/', views.MeetingDeleteView.as_view(), name='meeting_delete'),
]