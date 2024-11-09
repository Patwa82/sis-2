# exam_features/urls.py

from django.urls import path
from .views import ExamListView, ExamUploadView, StudentSubmissionView, StudentSubmissionListView, GradeUploadView

urlpatterns = [
    path('', ExamListView.as_view(), name='exam_list'),
    path('upload/', ExamUploadView.as_view(), name='exam_upload'),
    path('<int:pk>/submit/', StudentSubmissionView.as_view(), name='student_submission'),
    path('submissions/', StudentSubmissionListView.as_view(), name='student_submission_list'),
    path('grades/upload/', GradeUploadView.as_view(), name='upload_grade'),
]
