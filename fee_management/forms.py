from django import forms
from .models import FeePayment, Penalty
from course_management.models import CollegeProgram  # Use CollegeProgram instead of Course

class FeePaymentForm(forms.ModelForm):
    class Meta:
        model = FeePayment
        fields = ['student', 'program', 'branch', 'year', 'amount', 'payment_date', 'receipt_number', 'is_online']

    payment_date = forms.DateField(widget=forms.SelectDateWidget)
    branch = forms.CharField(max_length=100, label="Branch")
    year = forms.IntegerField(min_value=1, max_value=4, label="Year")

class PenaltyForm(forms.ModelForm):
    class Meta:
        model = Penalty
        fields = ['student', 'program', 'penalty_amount', 'reason', 'penalty_date']

    penalty_date = forms.DateField(widget=forms.SelectDateWidget)
