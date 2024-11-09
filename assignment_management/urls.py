# assignment_management/urls.py

from django.urls import path
from .views import (
    StudentAssignmentListView,
    StudentAssignmentDetailView,  # Ensure this view is imported
    StudentAssignmentSubmitView,
    FacultyAssignmentListView,
    FacultyAssignmentDetailView,
    FacultyAssignmentFeedbackView,
    FacultyAssignmentUploadView,
)

urlpatterns = [
    path('student/assignments/', StudentAssignmentListView.as_view(), name='student_assignment_list'),
    path('student/assignments/<int:pk>/', StudentAssignmentDetailView.as_view(), name='student_assignment_detail'),
    path('student/assignments/submit/', StudentAssignmentSubmitView.as_view(), name='student_assignment_submit'),
    path('faculty/assignments/', FacultyAssignmentListView.as_view(), name='faculty_assignment_list'),
    path('faculty/assignments/upload/', FacultyAssignmentUploadView.as_view(), name='faculty_assignment_upload'),
    path('faculty/assignments/<int:pk>/', FacultyAssignmentDetailView.as_view(), name='faculty_assignment_detail'),
    path('faculty/assignments/feedback/', FacultyAssignmentFeedbackView.as_view(), name='faculty_assignment_feedback'),
]
