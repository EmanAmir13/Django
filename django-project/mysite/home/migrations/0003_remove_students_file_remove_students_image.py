# Generated by Django 5.0 on 2023-12-20 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_students_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='file',
        ),
        migrations.RemoveField(
            model_name='students',
            name='image',
        ),
    ]
