# communication_tools/urls.py

from django.urls import path
from .views import DiscussionForumListView, DiscussionForumCreateView, NotificationListView

urlpatterns = [
    path('', DiscussionForumListView.as_view(), name='forum_list'),
    path('create/', DiscussionForumCreateView.as_view(), name='forum_create'),
    path('notifications/', NotificationListView.as_view(), name='notification_list'),
]
