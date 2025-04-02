from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'portfolio_app/index.html')


def student(request):
    return render(request, 'portfolio_app/student.html')

def projects(request):
    return render(request, 'portfolio_app/projects.html')