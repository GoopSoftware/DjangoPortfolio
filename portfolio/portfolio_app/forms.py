from django import forms
from .models import Portfolio, Student


class PortfolioForm(forms.ModelForm):
    model = Portfolio
    fields = ['title', 'contact_email', 'is_active', 'about', 'portfolio_image']

class StudentForm(forms.ModelForm):
    model = Student
    fields = ['name', 'email', 'Major', 'student_image']