# library_management/views.py

from django.views.generic import ListView, CreateView, UpdateView
from .models import Resource, Booking
from .forms import BookingForm  # Import the newly created form
from django.urls import reverse_lazy

class ResourceListView(ListView):
    model = Resource
    template_name = 'library_management/resource_booking.html'
    context_object_name = 'resources'

class BookingCreateView(CreateView):
    model = Booking
    form_class = BookingForm  # Use the custom form
    template_name = 'library_management/booking_create.html'
    success_url = reverse_lazy('resource_list')

    def form_valid(self, form):
        form.instance.booked_by = self.request.user  # Automatically assign the logged-in user
        return super().form_valid(form)


# library_management/views.py

from .forms import ResourceForm

# View for creating a new resource
class ResourceCreateView(CreateView):
    model = Resource
    form_class = ResourceForm
    template_name = 'library_management/resource_create.html'
    success_url = reverse_lazy('resource_list')

# View for updating an existing resource
class ResourceUpdateView(UpdateView):
    model = Resource
    form_class = ResourceForm
    template_name = 'library_management/resource_update.html'
    success_url = reverse_lazy('resource_list')
