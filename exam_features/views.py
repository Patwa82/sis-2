# exam_features/views.py

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import Exam, StudentSubmission, Grade
from .forms import ExamUploadForm, StudentSubmissionForm, GradeUploadForm

class ExamUploadView(CreateView):
    model = Exam
    form_class = ExamUploadForm
    template_name = 'exam_features/upload_exam.html'
    success_url = reverse_lazy('exam_list')

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)

class StudentSubmissionView(CreateView):
    model = StudentSubmission
    form_class = StudentSubmissionForm
    template_name = 'exam_features/submit_exam.html'
    success_url = reverse_lazy('student_submission_list')

    def form_valid(self, form):
        exam = get_object_or_404(Exam, pk=self.kwargs['pk'])
        if not exam.is_exam_active():
            return HttpResponseForbidden("This exam is not currently active.")
        form.instance.student = self.request.user
        return super().form_valid(form)

class ExamListView(ListView):
    model = Exam
    template_name = 'exam_features/exam_list.html'
    context_object_name = 'exams'

class StudentSubmissionListView(ListView):
    model = StudentSubmission
    template_name = 'exam_features/student_submission_list.html'
    context_object_name = 'submissions'

class GradeUploadView(CreateView):
    model = Grade
    form_class = GradeUploadForm
    template_name = 'exam_features/upload_grade.html'
    success_url = reverse_lazy('exam_list')
