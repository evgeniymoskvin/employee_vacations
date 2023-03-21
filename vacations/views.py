import datetime
from django.shortcuts import render, redirect
from django.views import View
from django.core import serializers
from django.http import JsonResponse
from django.db.models import Q
from .models import EmployeeModel, VacationsModel
from .forms import AddVacationForm, AddEmployeeForm


class IndexView(View):
    dt_now = datetime.datetime.now()

    def get(self, request, dt=dt_now.year):
        form = AddVacationForm()
        dt = 2023
        data_all = VacationsModel.objects.filter(
            Q(vacation_start__gte=f"{dt}-01-01") | Q(vacation_end__lte=f"{dt}-12-31")).filter(
            vacation_start__lt=f"{dt + 1}-01-01").filter(vacation_end__gt=f"{dt - 1}-12-31")
        # data_all = VacationsModel.objects.all()
        content = {"data": data_all,
                   "year": dt,
                   "form": form,
                   }
        return render(request, "vacations/index.html", content)

    def post(self, request):
        """post запрос со страницы поиска"""
        if request.POST.get('delete-id'):
            delete_id = int(request.POST.get('delete-id'))
            obj = VacationsModel.objects.get(id=delete_id)
            obj.delete()

        if request.POST.get('change-id'):
            start_date = request.POST.get('input-date-start')
            end_date = request.POST.get('input-date-end')
            change_id = int(request.POST.get('change-id'))
            print(change_id)
            if end_date > start_date:
                obj = VacationsModel.objects.get(id=change_id)
                obj.vacation_start = start_date
                obj.vacation_end = end_date
                obj.save()
                print(obj)
            else:
                print("Неправильная дата")

        data_all = VacationsModel.objects.all()
        content = {"data": data_all}
        return render(request, "vacations/index.html", content)


class AddNewVacationView(View):
    def post(self, request):
        form = AddVacationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(f'index')


class ChangeEmployeeView(View):
    def get(self, request):
        form_add_employee = AddEmployeeForm()
        data_employee = EmployeeModel.objects.all()
        content = {"data_employee": data_employee,
                   "employee_form": form_add_employee}
        return render(request, "vacations/edit_employee.html", content)

    def post(self, request):
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(f'employees')

class DeleteEmployeeView(View):
    def post(self, request):
        delete_emp_id = int(request.POST.get('delete-emp-id'))
        obj = EmployeeModel.objects.get(id=delete_emp_id)
        print(obj)
        obj.delete()
        return redirect(f'employees')
