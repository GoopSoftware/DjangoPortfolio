from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),

    path('students/', views.student, name='student'),
    path('students/<int:id>/',
         views.student_detail,
         name='student-detail'),

    path('projects/', views.projects, name='projects'),
    path('projects/<int:id>/',
         views.project_detail,
         name='project-detail'),

    path(
        'portfolio/<int:id>/',
        views.portfolio_detail,
        name='portfolio-detail'
    ),

]