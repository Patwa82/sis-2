from django.views.generic import ListView, DetailView, CreateView
from .models import CollegeProgram, Branch, Subject
from .forms import CollegeProgramForm
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import render

# ListView for College Programs
class CollegeProgramListView(ListView):
    model = CollegeProgram
    template_name = 'course_management/college_program_list.html'
    context_object_name = 'programs'

# CreateView for College Programs
class CollegeProgramCreateView(CreateView):
    model = CollegeProgram
    form_class = CollegeProgramForm
    template_name = 'course_management/college_program_create.html'
    success_url = reverse_lazy('college_program_list')

# DetailView for College Programs
class CollegeProgramDetailView(DetailView):
    model = CollegeProgram
    template_name = 'course_management/college_program_detail.html'

# New BranchListView to show branches related to programs
class BranchListView(ListView):
    model = Branch
    template_name = 'course_management/branch_list.html'
    context_object_name = 'branches'

    def get_queryset(self):
        program_id = self.request.GET.get('program_id')
        if program_id:
            return Branch.objects.filter(program_id=program_id)
        return Branch.objects.all()

# For fetching branches based on the selected program
def get_branches(request):
    program_id = request.GET.get('program_id')
    branches = Branch.objects.filter(program_id=program_id)
    branch_list = [{'id': branch.id, 'name': branch.name} for branch in branches]
    return JsonResponse({'branches': branch_list})

# View to show all program details including branches and subjects
def all_program_details(request):
    programs = CollegeProgram.objects.all()
    branches = Branch.objects.all()
    subjects = Subject.objects.all()
    
    context = {
        'programs': programs,
        'branches': branches,
        'subjects': subjects,
    }
    return render(request, 'course_management/all_program_details.html', context)
