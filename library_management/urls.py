# library_management/urls.py

from django.urls import path
from .views import ResourceListView, BookingCreateView

urlpatterns = [
    path('resources/', ResourceListView.as_view(), name='resource_list'),
    path('booking/create/', BookingCreateView.as_view(), name='booking_create'),
]
