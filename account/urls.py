from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout_view'),
    path('reset-password/', views.reset_password, name='reset_password'),
    path('student/', views.student, name='student'),
    path('parent/', views.parent, name='parent'),
    path('faculty/', views.faculty, name='faculty'),
    path('coordinator/', views.coordinator, name='coordinator'),
]
