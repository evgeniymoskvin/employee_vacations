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
from django.contrib.auth.views import LogoutView, LoginView
from . import views

urlpatterns = [
    path('chart/', views.ChartView.as_view(), name='chart'),
    path('', views.IndexView.as_view(), name='index'),
    path('employees/', views.ChangeEmployeeView.as_view(), name='employees'),
    path('add/vacation/', views.AddNewVacationView.as_view(), name='add-vacation'),
    path('delete/employee/', views.DeleteEmployeeView.as_view(), name='delete-employee'),
    path('change/employee/', views.ChangeNameEmployeeView.as_view(), name='change-employee'),
    path('modal-login', LoginView.as_view(), name='login-modal'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('test/', views.TestView.as_view() , name='test'),
    path('user/filters/', views.UserFilterView.as_view(), name='user-filter'),
    path('user/filters/clear', views.ClearFilterView.as_view(), name='user-filter-clear')

]
