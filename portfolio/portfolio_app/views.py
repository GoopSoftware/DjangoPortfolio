from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Portfolio, Student

# Create your views here.
def index(request):
    portfolios = Portfolio.objects.all()
    return render(request,
                  'portfolio_app/index.html',
                  {'portfolios': portfolios})

def student(request):
    return render(request, 'portfolio_app/student.html')

def projects(request):
    return render(request, 'portfolio_app/projects.html')

def portfolio_detail(request, id):
    #portfolio = get_object_or_404(Portfolio, id=id)
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
