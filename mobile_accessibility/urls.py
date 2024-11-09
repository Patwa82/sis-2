# mobile_accessibility/urls.py

from django.urls import path
from .views import MobileNotificationListView, MobileNotificationCreateView

urlpatterns = [
    path('notifications/', MobileNotificationListView.as_view(), name='mobile_notification_list'),
    path('notifications/create/', MobileNotificationCreateView.as_view(), name='mobile_notification_create'),
]
