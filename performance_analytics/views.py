# performance_analytics/views.py

from django.views.generic import ListView, CreateView
from .models import StudentPerformance
from .forms import StudentPerformanceForm
from exam_features.models import Exam, Grade
from django.urls import reverse_lazy
from django.db.models import Avg, Max, Min
from django.contrib.auth.mixins import LoginRequiredMixin

# View for student-specific performance analytics
class StudentAnalyticsListView(LoginRequiredMixin, ListView):
    model = StudentPerformance
    template_name = 'performance_analytics/student_analytics.html'
    context_object_name = 'performances'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student_performance = StudentPerformance.objects.filter(student=self.request.user)  # Fetch performance data for logged-in user
        context['student_performance'] = student_performance

        # Learning progress over time
        student_progress = student_performance.order_by('date')
        context['student_progress'] = student_progress

        return context

# Create student performance entry
class StudentPerformanceCreateView(CreateView):
    model = StudentPerformance
    form_class = StudentPerformanceForm
    template_name = 'performance_analytics/student_performance_create.html'
    success_url = reverse_lazy('student_analytics')

    def form_valid(self, form):
        return super().form_valid(form)

# View for overall exam result analytics
class ExamResultAnalyticsView(LoginRequiredMixin, ListView):
    model = Exam
    template_name = 'performance_analytics/exam_analytics.html'
    context_object_name = 'exam_analytics'

    def get_queryset(self):
        # Aggregate exam results including grade
        return Exam.objects.annotate(
            average_score=Avg('studentexamsubmission__score'),
            highest_score=Max('studentexamsubmission__score'),
            lowest_score=Min('studentexamsubmission__score')
        )
