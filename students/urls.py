from django.urls import path
from . import views

urlpatterns = [
    # Example:
    path('', views.student_list, name='student-list'),
]