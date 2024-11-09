from django.contrib import admin
from .models import FeePayment, Penalty

class FeePaymentAdmin(admin.ModelAdmin):
    list_display = ['student', 'program', 'branch', 'year', 'amount', 'payment_date', 'receipt_number', 'is_online']
    search_fields = ['student__username', 'receipt_number']  # Use 'student__username' to search by username
    list_filter = ['payment_date', 'program', 'branch', 'year', 'is_online']

class PenaltyAdmin(admin.ModelAdmin):
    list_display = ['student', 'program', 'penalty_amount', 'penalty_date']
    search_fields = ['student__username']  # Use 'student__username' to search by username
    list_filter = ['penalty_date', 'program']

admin.site.register(FeePayment, FeePaymentAdmin)
admin.site.register(Penalty, PenaltyAdmin)
