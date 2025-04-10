# Generated by Django 5.1.6 on 2025-04-03 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0006_remove_portfolio_project_project_portfolio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='portfolio_image',
            field=models.ImageField(blank=True, null=True, upload_to='portfolios/'),
        ),
        migrations.AddField(
            model_name='student',
            name='student_image',
            field=models.ImageField(blank=True, null=True, upload_to='students/'),
        ),
    ]
