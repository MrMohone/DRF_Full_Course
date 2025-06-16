from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("employees", views.EmployeeViewSet, basename="employee") # don't use '👉/' in 'employees, also '👉.as_view' in 'EmployeeViewSet' 

urlpatterns = [
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentsDetailView),
    
    #class based
    # path('employees/', views.Employees.as_view()),
    # path("employees/<int:pk>/", views.EmployeesDetail.as_view())
    
    #For ViewSets 
    path("", include(router.urls))
    
]
