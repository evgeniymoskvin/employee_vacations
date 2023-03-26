import datetime
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.db.models import Q
from .models import EmployeeModel, VacationsModel
from .forms import AddVacationForm, AddEmployeeForm, LoginForm


class IndexView(View):
    """Главная страница"""
    def get(self, request):
        form_login = LoginForm()
        content = {
            "login_form": form_login,
        }
        return render(request, 'vacations/index.html', content)


class ChartView(View):
    """Страница с графиком отпусков сотрудников"""
    dt_now = datetime.datetime.now()

    @method_decorator(login_required(login_url='index'))
    def get(self, request, dt=dt_now.year):
        form = AddVacationForm()
        dt = 2023
        data_all = VacationsModel.objects.filter(
            Q(vacation_start__gte=f"{dt}-01-01") | Q(vacation_end__lte=f"{dt}-12-31")).filter(
            vacation_start__lt=f"{dt + 1}-01-01").filter(vacation_end__gt=f"{dt - 1}-12-31")
        # data_all = VacationsModel.objects.all()
        vacation_in_this_month = []
        for empl in data_all:
            if empl.vacation_start.year == datetime.datetime.now().year or empl.vacation_end.year == datetime.datetime.now().year:
                if empl.vacation_start.month == datetime.datetime.now().month or empl.vacation_end.month == datetime.datetime.now().month:
                    print(empl)
                    vacation_in_this_month.append(empl)

        print(datetime.datetime.now().month)
        print(vacation_in_this_month)

        content = {"data": data_all,
                   "year": dt,
                   "form": form,

                   }
        return render(request, "vacations/chart.html", content)

    def post(self, request):
        """Изменение или удаление отпуска сотрудника"""
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
        return render(request, "vacations/chart.html", content)


class AddNewVacationView(View):
    """Добавления нового отпуска сотруднику"""
    def post(self, request):
        form = AddVacationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(f'chart')


class ChangeEmployeeView(View):
    """Страница редактирования списка сотрудников"""
    def get(self, request):
        """Получение списка сотрудников"""
        form_add_employee = AddEmployeeForm()
        data_employee = EmployeeModel.objects.all()
        content = {"data_employee": data_employee,
                   "employee_form": form_add_employee}
        return render(request, "vacations/edit_employee.html", content)

    def post(self, request):
        """Запись нового сотрудника"""
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(f'employees')


class DeleteEmployeeView(View):
    """Удаление сотрудника"""
    def post(self, request):
        if request.POST.get('delete-emp-id'):
            delete_emp_id = int(request.POST.get('delete-emp-id'))
            obj = EmployeeModel.objects.get(id=delete_emp_id)
            print(obj)
            obj.delete()
        return redirect(f'employees')


class ChangeNameEmployeeView(View):
    """Изменение ФИО сотрудника"""
    def post(self, request):
        if request.POST.get('change-emp-id'):
            change_emp_id = int(request.POST.get('change-emp-id'))
            obj = EmployeeModel.objects.get(id=change_emp_id)
            obj.first_name = request.POST.get('input_first_name_change')
            obj.last_name = request.POST.get('input_last_name_change')
            obj.middle_name = request.POST.get('input_middle_name_change')
            obj.save()
        return redirect(f'employees')
