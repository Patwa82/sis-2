from django.urls import path
from .views import SupportRequestListView, SupportRequestCreateView

urlpatterns = [
    path('', SupportRequestListView.as_view(), name='support_request_list'),
    path('create/', SupportRequestCreateView.as_view(), name='support_request_create'),
]
