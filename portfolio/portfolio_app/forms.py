from django import forms
from .models import Portfolio, Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'Major', 'student_image']

    def save(self, commit=True):
        student = super().save(commit=False)
        portfolio = Portfolio.objects.create(
            title=f"{student.name}'s Portfolio",
            contact_email=student.email
        )
        student.portfolio = portfolio
        if commit:
            student.save()
        return student