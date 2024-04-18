from django.db import models
from django.utils.dateparse import parse_date

# from django.core.validators import MaxValueValidator

# Create your models here.
class Gradebook(models.Model):
    assignment_name = models.CharField(max_length=20)
    percentage = models.IntegerField(default = 0)
    student_name = models.CharField(max_length=20)
    date = models.DateField()
    notes = models.TextField(default = None, null = True)

def validate_date_format(value):
    try:
        parse_date(value)
    except:
        raise ValueError

def create_grade(assignment, percentage, name, date, notes=None):
    if not 0 <= percentage <= 100:
        raise ValueError
    
    validate_date_format(date)

    return Gradebook.objects.create(assignment_name = assignment, percentage = percentage, student_name = name, date = date, notes = notes)

def find_grade(id):
    try:
        return Gradebook.objects.get(id = id)
    except:
        raise ValueError
    
def update_percentage(id, percentage):
    if not 0 <= percentage <= 100:
        raise ValueError
    try:
        grade = find_grade(id = id)
        grade.percentage = percentage
        grade.save()
        return grade
    except:
        raise ValueError
    
def update_notes(id, notes):
    try:
        grade = find_grade(id = id)
        grade.notes = notes
        grade.save()
        return grade
    except:
        raise ValueError

def delete_grade(id):
    try:
        return find_grade(id = id).delete()
    except:
        raise ValueError
    
def all_grades():
    return Gradebook.objects.all()
    
def filter_grades(name):
    return Gradebook.objects.filter(student_name = name)
    
def filter_assignments(assignment):
    return Gradebook.objects.filter(assignment_name = assignment)
    
def filter_grades_greaterthan(assignment, percentage):
    if not 0 <= percentage <= 100:
        raise ValueError
    return Gradebook.objects.filter(assignment_name = assignment, percentage__gte=percentage)
