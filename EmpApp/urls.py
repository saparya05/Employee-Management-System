from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('add-employee/', views.add_employee, name='add-employee'),
  path('view-employee/', views.view_employee, name='view-employee'),
  path('update-employee/<int:pk>/', views.update_employee, name='update-employee'),
  path('delete-employee/<int:pk>/', views.delete_employee, name='delete-employee'),
]
