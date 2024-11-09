# communication_tools/views.py

from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import DiscussionForum, Notification
from .forms import DiscussionForumForm
from django.urls import reverse_lazy
from django.conf import settings

class DiscussionForumListView(ListView):
    model = DiscussionForum
    template_name = 'communication_tools/discussion_forum.html'
    context_object_name = 'forums'

    def get_queryset(self):
        return DiscussionForum.objects.all()

class DiscussionForumCreateView(CreateView):
    model = DiscussionForum
    template_name = 'communication_tools/discussion_forum_create.html'
    form_class = DiscussionForumForm
    success_url = reverse_lazy('forum_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        # Assuming your settings.AUTH_USER_MODEL includes a relationship to programs (e.g., user.profile.programs)
        for user in settings.AUTH_USER_MODEL.objects.filter(profile__program=self.object.program):
            Notification.objects.create(user=user, message=f"New discussion created: {self.object.title}")
        return response

class NotificationListView(ListView):
    model = Notification
    template_name = 'communication_tools/notification_list.html'
    context_object_name = 'notifications'

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user).order_by('-created_at')
