from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from .models import Portfolio, Student, Project
from .forms import PortfolioForm, StudentForm

# Create your views here.
def index(request):
    portfolios = Portfolio.objects.all()
    return render(request,
                  'portfolio_app/index.html',
                  {'portfolios': portfolios})

def student(request):
    student = Student.objects.all()
    return render(request,
                  'portfolio_app/student.html',
                  {
                      'students': student
        }
    )

def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    portfolio = student.portfolio


    return render(
        request,
        'portfolio_app/student_detail.html',
        {
            'student': student,
            'portfolio': portfolio,
            'projects': portfolio.projects.all()
        }
    )

def projects(request):
    projects = Project.objects.all()

    return render(
        request,
        'portfolio_app/projects.html',
        {
            'projects': projects,
        }
    )

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)

    return render(
        request,
        'portfolio_app/project_detail.html',
        {
            'project': project
        }

    )

def portfolio_detail(request, id):
    student = get_object_or_404(Student, id=id)
    portfolio = student.portfolio

    return render(
        request,
        'portfolio_app/portfolio_detail.html',
        {
            'portfolio': portfolio,
            'student': student,
            'projects': portfolio.projects.all()
        }
    )
