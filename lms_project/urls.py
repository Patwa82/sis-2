"""
URL configuration for lms_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('courses/', include('course_management.urls')),  
    path('assignments/', include('assignment_management.urls')),  
    path('attendance/', include('attendance_management.urls')),
    path('forums/', include('communication_tools.urls')),
    path('exams/', include('exam_features.urls')),  # Use 'exam_features' instead of 'examination_features'    
    path('analytics/', include('performance_analytics.urls')),  
    path('parent-portal/', include('parent_portal.urls')),  
    path('library/', include('library_management.urls')),  
    path('schedule/', include('class_rescheduling.urls')),
    path('support/', include('student_support.urls')), 
    path('fee/', include('fee_management.urls')),
    path('mobile/', include('mobile_accessibility.urls')),
    path('security/', include('data_security.urls')),
    path('security/', include('security.urls')),
    path('', include('account.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
