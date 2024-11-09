from django.views.generic import ListView, CreateView
from .models import FeePayment, Penalty
from .forms import FeePaymentForm, PenaltyForm
from django.urls import reverse_lazy

# View for listing all fee payments
class FeePaymentListView(ListView):
    model = FeePayment
    template_name = 'fee_management/fee_payment_list.html'
    context_object_name = 'payments'

# View for creating new fee payments
class FeePaymentCreateView(CreateView):
    model = FeePayment
    form_class = FeePaymentForm
    template_name = 'fee_management/fee_payment_create.html'
    success_url = reverse_lazy('fee_payment_list')

# View for creating penalties
class PenaltyCreateView(CreateView):
    model = Penalty
    form_class = PenaltyForm
    template_name = 'fee_management/penalty_create.html'
    success_url = reverse_lazy('fee_payment_list')
