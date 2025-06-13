from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student

def studentsView(request):
    students = Student.objects.all()
    student_list = list(students.values())
    return JsonResponse(student_list, safe=False)