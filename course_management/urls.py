from django.urls import path
from .views import CollegeProgramListView, CollegeProgramCreateView, CollegeProgramDetailView, BranchListView, get_branches, all_program_details

urlpatterns = [
    path('programs/', CollegeProgramListView.as_view(), name='college_program_list'),
    path('programs/create/', CollegeProgramCreateView.as_view(), name='college_program_create'),
    path('programs/<int:pk>/', CollegeProgramDetailView.as_view(), name='college_program_detail'),
    path('branches/', BranchListView.as_view(), name='branch_list'),
    path('get-branches/', get_branches, name='get_branches'),
    path('all-details/', all_program_details, name='all_program_details'),
]