import datetime
import json

from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import EmployeeModel, VacationsModel, VacationTypeModel, DepartmentModel, EmployeeAccessWriteModel, \
    AccessLevelModel, WritePermissionModel, JobTitleModel, CommandNumberModel, UserFilterModel
from .forms import AddVacationForm, AddEmployeeForm, LoginForm, FilterForm, YearForm


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
        user = EmployeeModel.objects.get(user=request.user)
        try:
            user_filters = UserFilterModel.objects.get(employee=user)
        except:
            user_filters = UserFilterModel.objects.create(employee=user, year_filter=dt,
                                                          department_filter=user.department_user,
                                                          command_number_filter=user.command_number_user)
            user_filters.save()

        get_user_permission = EmployeeAccessWriteModel.objects.get(employee=user.id).access_level.id
        form_add_vacation = AddVacationForm()
        form_add_vacation.fields['employee'].queryset = EmployeeModel.objects.filter(
            command_number_user=user.command_number_user)
        form_year_filter = YearForm()
        form_filter = FilterForm()
        # Для руководителей управления фильтруем отделы только их управления
        if get_user_permission == 2:
            form_filter.fields['command_number_filter'].queryset = CommandNumberModel.objects.filter(
                department=user.department_user)

        dt = user_filters.year_filter
        flag_add_vacation = EmployeeAccessWriteModel.objects.get(employee=user.id).write_permission
        # Объявляем пустую переменную с отпусками для исключения ошибки
        data_all = VacationsModel.objects.none()

        if get_user_permission == 3:
            # Если права пользователя == 3 (отдел) то фильтруем данные по году, а так же по отделу
            data_all = VacationsModel.objects.filter(
                Q(vacation_start__gte=f"{dt}-01-01") | Q(vacation_end__lte=f"{dt}-12-31")).filter(
                vacation_start__lt=f"{dt + 1}-01-01").filter(vacation_end__gt=f"{dt - 1}-12-31").filter(
                employee__command_number_user_id=user.command_number_user_id)
        elif get_user_permission == 2:
            # Если права пользователя == 2 (управление) то фильтруем данные по году, а так же по управлению
            filter_user = UserFilterModel.objects.get(employee__user=request.user)
            # Если фильтр по отделам True то фильтруем по отделам
            if filter_user.use_command_number_filter is True:
                data_all = VacationsModel.objects.filter(
                    Q(vacation_start__gte=f"{dt}-01-01") | Q(vacation_end__lte=f"{dt}-12-31")).filter(
                    vacation_start__lt=f"{dt + 1}-01-01").filter(vacation_end__gt=f"{dt - 1}-12-31").filter(
                    employee__command_number_user_id=filter_user.command_number_filter_id)
            else:
                data_all = VacationsModel.objects.filter(
                    Q(vacation_start__gte=f"{dt}-01-01") | Q(vacation_end__lte=f"{dt}-12-31")).filter(
                    vacation_start__lt=f"{dt + 1}-01-01").filter(vacation_end__gt=f"{dt - 1}-12-31").filter(
                    employee__department_user_id=user.department_user_id)
        elif get_user_permission == 1:
            # Если права просмотра == 1 (полные)
            filter_user = UserFilterModel.objects.get(employee__user=request.user)
            # Получаем настройки фильтров, если оба False то фильтруем данные только по году
            if filter_user.use_department_filter is False and filter_user.use_command_number_filter is False:
                data_all = VacationsModel.objects.filter(
                    Q(vacation_start__gte=f"{dt}-01-01") | Q(vacation_end__lte=f"{dt}-12-31")).filter(
                    vacation_start__lt=f"{dt + 1}-01-01").filter(vacation_end__gt=f"{dt - 1}-12-31")
            # Получаем настройки фильтров, если управление True, а отдел False, то фильтруем данные по году и управлению
            elif filter_user.use_department_filter is True and filter_user.use_command_number_filter is False:
                data_all = VacationsModel.objects.filter(
                    Q(vacation_start__gte=f"{dt}-01-01") | Q(vacation_end__lte=f"{dt}-12-31")).filter(
                    vacation_start__lt=f"{dt + 1}-01-01").filter(vacation_end__gt=f"{dt - 1}-12-31").filter(
                    employee__department_user_id=filter_user.department_filter_id)
            # Получаем настройки фильтров, если отдел True, то фильтруем данные по году и отделу
            elif filter_user.use_command_number_filter is True:
                data_all = VacationsModel.objects.filter(
                    Q(vacation_start__gte=f"{dt}-01-01") | Q(vacation_end__lte=f"{dt}-12-31")).filter(
                    vacation_start__lt=f"{dt + 1}-01-01").filter(vacation_end__gt=f"{dt - 1}-12-31").filter(
                    employee__command_number_user_id=filter_user.command_number_filter_id)

        data_all = data_all.order_by('employee__last_name')

        vacation_in_this_month = []
        for empl in data_all:
            if empl.vacation_start.year == datetime.datetime.now().year or empl.vacation_end.year == datetime.datetime.now().year:
                if empl.vacation_start.month == datetime.datetime.now().month or empl.vacation_end.month == datetime.datetime.now().month:
                    vacation_in_this_month.append(empl)

        content = {"data": data_all,
                   "year": dt,
                   "form_add_vacation": form_add_vacation,
                   "flag_add_vacation": flag_add_vacation,
                   "filter_form": form_filter,
                   "permission": get_user_permission,
                   'form_year_filter': form_year_filter,
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
        user = EmployeeModel.objects.get(user=request.user)
        flag_add_vacation = EmployeeAccessWriteModel.objects.get(employee=user.id).write_permission
        form_add_employee = AddEmployeeForm()
        get_user_permission = EmployeeAccessWriteModel.objects.get(employee=user.id).access_level.id
        data_employee = EmployeeModel.objects.none()
        if get_user_permission == 3:
            # Если права пользователя == 3 (отдел) то фильтруем по отделу
            data_employee = EmployeeModel.objects.filter(command_number_user=user.command_number_user)
        elif get_user_permission == 2:
            # Если права пользователя == 2 (управление) то фильтруем по управлению
            data_employee = EmployeeModel.objects.filter(department_user=user.department_user)
        elif get_user_permission == 1:
            # Если права просмотра == 1 (полные) то показываем всех
            data_employee = EmployeeModel.objects.all()

        # Фильтруем сотрудников по свойству отображения и сортируем по фамилии
        data_employee = data_employee.filter(show_employee=True).order_by('last_name')
        content = {"data_employee": data_employee,
                   "employee_form": form_add_employee,
                   "flag_add_vacation": flag_add_vacation}
        return render(request, "vacations/edit_employee.html", content)

    def post(self, request):
        """Запись нового сотрудника"""
        user = EmployeeModel.objects.get(user=request.user)
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            new_emp = form.save(commit=False)
            new_emp.department_user = user.department_user
            new_emp.command_number_user = user.command_number_user
            form.save()
        return redirect(f'employees')


class DeleteEmployeeView(View):
    """Удаление сотрудника"""

    def post(self, request):
        if request.POST.get('delete-emp-id'):
            delete_emp_id = int(request.POST.get('delete-emp-id'))
            obj = EmployeeModel.objects.get(id=delete_emp_id)
            print(obj)
            obj.show_employee = False
            obj.save()
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


class TestView(View):
    """Тестовый календарь"""

    def get(self, request):
        dt = 2023
        data_all = VacationsModel.objects.filter(
            Q(vacation_start__gte=f"{dt}-01-01") | Q(vacation_end__lte=f"{dt}-12-31")).filter(
            vacation_start__lt=f"{dt + 1}-01-01").filter(vacation_end__gt=f"{dt - 1}-12-31")
        # data_all = VacationsModel.objects.all()
        dict_vac = {}
        list_ = []
        delta = datetime.timedelta(days=1)
        for empl in data_all:
            start_date = empl.vacation_start
            end_date = empl.vacation_end
            while (start_date <= end_date):
                list_.append([f'{empl.employee.first_name} {empl.employee.last_name} {empl.employee.middle_name}',
                              start_date.year, start_date.month, start_date.day])
                start_date += delta

        content = {"data_all": data_all,
                   "json_data": json.dumps(list_, ensure_ascii=False)}
        return render(request, 'vacations/test.html', content)


class UserFilterView(View):
    """Изменение ФИО сотрудника"""

    def post(self, request):
        print(request.POST.get)

        filter_user = UserFilterModel.objects.get(employee__user=request.user)

        if request.POST.get('year'):
            filter_user.year_filter = request.POST.get('year')
        if request.POST.get('department_filter'):
            filter_user.department_filter_id = request.POST.get('department_filter')
            filter_user.use_department_filter = True
        if request.POST.get('command_number_filter'):
            filter_user.command_number_filter_id = request.POST.get('command_number_filter')
            filter_user.use_command_number_filter = True

        filter_user.save()

        print(filter_user)

        return redirect(f'chart')


class ClearFilterView(View):
    """Сброс фильтров"""

    def get(self, request):
        filter_user = UserFilterModel.objects.get(employee__user=request.user)
        filter_user.use_department_filter = False
        filter_user.use_command_number_filter = False
        filter_user.save()
        print(f'Пользователь {request.user} сбросил фильтры')
        return redirect(f'chart')
