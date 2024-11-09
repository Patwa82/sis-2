# assignment_management/views.py

from django.views.generic import ListView, DetailView, CreateView
from .models import StudentAssignment, FacultyAssignment
from .forms import StudentAssignmentForm, FacultyAssignmentForm
from django.urls import reverse_lazy
from django.utils import timezone

class StudentAssignmentListView(ListView):
    model = StudentAssignment
    template_name = 'assignment_management/student_assignment_list.html'
    context_object_name = 'assignments'

class StudentAssignmentDetailView(DetailView):
    model = StudentAssignment
    template_name = 'assignment_management/student_assignment_detail.html'

class StudentAssignmentSubmitView(CreateView):
    model = StudentAssignment
    form_class = StudentAssignmentForm
    template_name = 'assignment_management/student_assignment_submit.html'
    success_url = reverse_lazy('student_assignment_list')

    def form_valid(self, form):
        assignment = form.save(commit=False)
        assignment.submitted = True
        assignment.submission_date = timezone.now().date()
        assignment.save()
        return super().form_valid(form)
    
# Faculty Views
class FacultyAssignmentListView(ListView):
    model = FacultyAssignment
    template_name = 'assignment_management/faculty_assignment_list.html'

class FacultyAssignmentDetailView(DetailView):
    model = FacultyAssignment
    template_name = 'assignment_management/faculty_assignment_detail.html'

class FacultyAssignmentUploadView(CreateView):
    model = FacultyAssignment
    form_class = FacultyAssignmentForm
    template_name = 'assignment_management/faculty_assignment_upload.html'
    success_url = reverse_lazy('faculty_assignment_list')

    def form_valid(self, form):
        faculty_assignment = form.save(commit=False)
        faculty_assignment.auto_grade_assignment()  # Call the auto-grading method
        faculty_assignment.save()
        return super().form_valid(form)
    
class FacultyAssignmentFeedbackView(CreateView):
    model = FacultyAssignment
    form_class = FacultyAssignmentForm
    template_name = 'assignment_management/faculty_assignment_feedback.html'
    success_url = reverse_lazy('faculty_assignment_list')


