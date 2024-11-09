# attendance_management/views.py

from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Attendance
from .forms import AttendanceForm
from django.utils import timezone

class AttendanceTrackingView(CreateView):
    model = Attendance
    form_class = AttendanceForm
    template_name = 'attendance_management/attendance_tracking.html'
    success_url = '/attendance/report/'  # Redirect to the attendance report page after submission

    def form_valid(self, form):
        attendance = form.save(commit=False)
        attendance.date = timezone.now().date()  # Set to today's date
        attendance.save()
        return super().form_valid(form)

class AttendanceReportView(ListView):
    model = Attendance
    template_name = 'attendance_management/attendance_report.html'
    context_object_name = 'attendances'

    def get_queryset(self):
        return Attendance.objects.all()  # Fetch all attendance records
