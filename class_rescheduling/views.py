from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import ClassSchedule, TimeTableNotification
from .forms import ClassScheduleForm, TimeTableNotificationForm

# Class Schedule Views
class ClassScheduleListView(ListView):
    model = ClassSchedule
    template_name = 'class_rescheduling/time_table.html'
    context_object_name = 'schedules'

    def get_queryset(self):
        # Optionally customize this method to filter schedules by program, instructor, etc.
        return ClassSchedule.objects.all()

class ClassScheduleCreateView(CreateView):
    model = ClassSchedule
    form_class = ClassScheduleForm
    template_name = 'class_rescheduling/class_schedule_create.html'
    success_url = reverse_lazy('class_schedule_list')

    def form_valid(self, form):
        form.instance.instructor = self.request.user  # Automatically set the logged-in user as the instructor
        return super().form_valid(form)

# Time Table Notification Views
class TimeTableNotificationListView(ListView):
    model = TimeTableNotification
    template_name = 'class_rescheduling/notification_list.html'
    context_object_name = 'notifications'

    def get_queryset(self):
        # Optionally customize this method to filter notifications by schedule, etc.
        return TimeTableNotification.objects.all()

class TimeTableNotificationCreateView(CreateView):
    model = TimeTableNotification
    form_class = TimeTableNotificationForm
    template_name = 'class_rescheduling/notification_create.html'
    success_url = reverse_lazy('notification_list')

    def form_valid(self, form):
        return super().form_valid(form)
