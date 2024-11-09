from django.views.generic import ListView, CreateView
from .models import SupportRequest
from .forms import SupportRequestForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin  # To ensure only logged-in users can submit requests

class SupportRequestListView(LoginRequiredMixin, ListView):
    model = SupportRequest
    template_name = 'student_support/support_request_list.html'
    context_object_name = 'requests'

    # Show only the support requests of the logged-in user
    def get_queryset(self):
        return SupportRequest.objects.filter(student=self.request.user)

class SupportRequestCreateView(LoginRequiredMixin, CreateView):
    model = SupportRequest
    form_class = SupportRequestForm
    template_name = 'student_support/support_request_create.html'
    success_url = reverse_lazy('support_request_list')

    def form_valid(self, form):
        form.instance.student = self.request.user  # Automatically set the logged-in user
        return super().form_valid(form)
