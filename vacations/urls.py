"""employee_vacations URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('index-2/', views.Index2View.as_view(), name='index-2'),
    path('employees/', views.ChangeEmployeeView.as_view(), name='employees'),
    path('add/vacation/', views.AddNewVacationView.as_view(), name='add-vacation'),
    path('delete/employee/', views.DeleteEmployeeView.as_view(), name='delete-employee'),
]
