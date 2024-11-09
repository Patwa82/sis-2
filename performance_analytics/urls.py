from django.urls import path
from .views import StudentAnalyticsListView, StudentPerformanceCreateView, ExamResultAnalyticsView

urlpatterns = [
    path('student/analytics/', StudentAnalyticsListView.as_view(), name='student_analytics'),
    path('student/performance/create/', StudentPerformanceCreateView.as_view(), name='student_performance_create'),
    path('exam/analytics/', ExamResultAnalyticsView.as_view(), name='exam_analytics'),
]
