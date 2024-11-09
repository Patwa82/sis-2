from django.urls import path
from .views import FeePaymentListView, FeePaymentCreateView, PenaltyCreateView

urlpatterns = [
    path('payments/', FeePaymentListView.as_view(), name='fee_payment_list'),
    path('payments/create/', FeePaymentCreateView.as_view(), name='fee_payment_create'),
    path('penalties/create/', PenaltyCreateView.as_view(), name='penalty_create'),
]
