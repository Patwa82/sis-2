# attendance_management/urls.py

from django.urls import path
from .views import AttendanceReportView, AttendanceTrackingView  # Ensure this includes AttendanceTrackingView

urlpatterns = [
    path('report/', AttendanceReportView.as_view(), name='attendance_report'),
    path('track/', AttendanceTrackingView.as_view(), name='track_attendance'),
]
