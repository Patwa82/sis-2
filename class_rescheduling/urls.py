from django.urls import path
from .views import ClassScheduleListView, ClassScheduleCreateView, TimeTableNotificationListView, TimeTableNotificationCreateView

urlpatterns = [
    # Class Schedule URLs
    path('', ClassScheduleListView.as_view(), name='class_schedule_list'),
    path('create/', ClassScheduleCreateView.as_view(), name='class_schedule_create'),

    # Time Table Notification URLs
    path('notifications/', TimeTableNotificationListView.as_view(), name='notification_list'),
    path('notifications/create/', TimeTableNotificationCreateView.as_view(), name='notification_create'),
]
