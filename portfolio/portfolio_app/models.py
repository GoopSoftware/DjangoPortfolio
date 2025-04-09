from django.db import models
from django.db.models import ImageField
from django.urls import reverse

# Create your models here.



class Portfolio(models.Model):

    title = models.CharField(max_length=200)
    contact_email = models.EmailField(max_length=200)
    is_active = models.BooleanField(default=True)
    about = models.TextField(blank=True)
    portfolio_image = ImageField(upload_to='portfolios/', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio-detail', args=[str(self.id)])


class Project(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    portfolio = models.ForeignKey(Portfolio,
                                  on_delete=models.CASCADE,
                                  default=1,
                                  related_name='projects')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project-detail', args=[str(self.id)])


class Student(models.Model):
    MAJOR = (
        ('CSM-BS', 'Computer Science Major, B.S.'),
        ('DSML-BS', 'Data Science and machine Learning Major, B.S.'),
        ('CSciM', 'Computer Science Minor'),
        ('CSecM', 'Computer Security Minor')
    )
    name = models.CharField(max_length=200)
    email = models.EmailField("MSU Denver Email", max_length=200)
    Major = models.CharField(max_length=200, choices=MAJOR)
    portfolio = models.OneToOneField(Portfolio, on_delete=models.CASCADE)

    student_image = models.ImageField(upload_to='students/', blank=True, null=True)
    # Fix the capital on Major next migration

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.id)])
