from django.urls import path
from .views import (
    ProgressReportListView,
    ProgressReportCreateView,
    BehaviorListView,
    BehaviorCreateView,
    EventNotificationListView,
    EventNotificationCreateView
)

urlpatterns = [
    path('progress-reports/', ProgressReportListView.as_view(), name='progress_report_list'),
    path('progress-reports/create/', ProgressReportCreateView.as_view(), name='progress_report_create'),
    path('behaviors/', BehaviorListView.as_view(), name='behavior_list'),
    path('behaviors/create/', BehaviorCreateView.as_view(), name='behavior_create'),
    path('event-notifications/', EventNotificationListView.as_view(), name='event_notification_list'),
    path('event-notifications/create/', EventNotificationCreateView.as_view(), name='event_notification_create'),
]
