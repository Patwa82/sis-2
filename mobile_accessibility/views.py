# mobile_accessibility/views.py

from django.views.generic import ListView, CreateView
from .models import MobileNotification
from .forms import MobileNotificationForm
from django.urls import reverse_lazy

# View for listing mobile notifications
class MobileNotificationListView(ListView):
    model = MobileNotification
    template_name = 'mobile_accessibility/mobile_app.html'
    context_object_name = 'notifications'

# View for creating new notifications
class MobileNotificationCreateView(CreateView):
    model = MobileNotification
    form_class = MobileNotificationForm
    template_name = 'mobile_accessibility/mobile_notification_create.html'
    success_url = reverse_lazy('mobile_notification_list')

    def form_valid(self, form):
        notification = form.save(commit=False)
        notification.sent_by = self.request.user  # Automatically set the logged-in user as the sender
        notification.save()
        return super().form_valid(form)
