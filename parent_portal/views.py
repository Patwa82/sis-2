from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import ProgressReport, Behavior, EventNotification
from django.contrib.auth.mixins import LoginRequiredMixin  # Ensure only logged-in users access these views
from .forms import ProgressReportForm, BehaviorForm, EventNotificationForm

# Progress Report Views
class ProgressReportListView(LoginRequiredMixin, ListView):
    model = ProgressReport
    template_name = 'parent_portal/progress_report.html'
    context_object_name = 'reports'

    def get_queryset(self):
        # If the user is a parent, they should see their child's reports
        if self.request.user.groups.filter(name='Parent').exists():
            return ProgressReport.objects.filter(student=self.request.user)
        # If the user is a faculty, they can see all reports they created
        elif self.request.user.groups.filter(name='Faculty').exists():
            return ProgressReport.objects.filter(faculty=self.request.user)
        # If the user is a student, they should see their own reports
        else:
            return ProgressReport.objects.filter(student=self.request.user)

class ProgressReportCreateView(LoginRequiredMixin, CreateView):
    model = ProgressReport
    form_class = ProgressReportForm
    template_name = 'parent_portal/progress_report_create.html'
    success_url = reverse_lazy('progress_report_list')

    def form_valid(self, form):
        form.instance.faculty = self.request.user  # Set the faculty as the logged-in user
        return super().form_valid(form)

# Behavior Views
class BehaviorListView(LoginRequiredMixin, ListView):
    model = Behavior
    template_name = 'parent_portal/behavior_list.html'
    context_object_name = 'behaviors'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Parent').exists():
            return Behavior.objects.filter(student=self.request.user)
        elif self.request.user.groups.filter(name='Faculty').exists():
            return Behavior.objects.all()  # Faculty can view all behaviors
        else:
            return Behavior.objects.filter(student=self.request.user)

class BehaviorCreateView(LoginRequiredMixin, CreateView):
    model = Behavior
    form_class = BehaviorForm
    template_name = 'parent_portal/behavior_create.html'
    success_url = reverse_lazy('behavior_list')

# Event Notification Views
class EventNotificationListView(LoginRequiredMixin, ListView):
    model = EventNotification
    template_name = 'parent_portal/event_notification_list.html'
    context_object_name = 'notifications'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Parent').exists():
            return EventNotification.objects.filter(student=self.request.user)
        elif self.request.user.groups.filter(name='Faculty').exists():
            return EventNotification.objects.all()  # Faculty can view all notifications
        else:
            return EventNotification.objects.filter(student=self.request.user)

class EventNotificationCreateView(LoginRequiredMixin, CreateView):
    model = EventNotification
    form_class = EventNotificationForm
    template_name = 'parent_portal/event_notification_create.html'
    success_url = reverse_lazy('event_notification_list')
