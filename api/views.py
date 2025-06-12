from django.shortcuts import render
from django.http import JsonResponse

def studentsView(request):
    student = {
        'id': 1,
        'name': 'Alice',
        'class' :  'Infromation System' 
        }
    return JsonResponse(student)