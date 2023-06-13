from .models import VacationsModel, EmployeeModel, UserFilterModel, YearModel
from django.forms import ModelForm, Select, NumberInput, DateInput, TextInput, CharField, PasswordInput, EmailInput
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.admin.widgets import AdminDateWidget


class DateInputCustom(DateInput):
    input_type = 'date'


class AddVacationForm(ModelForm):
    class Meta:
        model = VacationsModel
        exclude = [
            'vacation_end'
        ]

        widgets = {"employee": Select(attrs={"class": "form-select",
                                             "aria-label": "Сотрудник"}),

                   "vacation_start": DateInputCustom(attrs={"class": "form-control"}),
                   "day_count": NumberInput(attrs={"class": "form-control",
                                                   "aria-label": "Количество дней"}),
                   "vacation_type": Select(attrs={"class": "form-select",
                                                  "aria-label": "Вид отпуска"}),

                   }


class AddEmployeeForm(ModelForm):
    class Meta:
        model = EmployeeModel
        exclude = [
            'user',
            'work_status',
            'command_number_user',
            'department_user',

        ]

        widgets = {
            "first_name": TextInput(attrs={"class": "form-control",
                                           "aria-label": "Здание",
                                           'placeholder': 'Имя'}),
            "middle_name": TextInput(attrs={"class": "form-control",
                                            "aria-label": "Здание",
                                            'placeholder': 'Отчество'}),
            "last_name": TextInput(attrs={"class": "form-control",
                                          "aria-label": "Здание",
                                          'placeholder': 'Фамилия'}),
            "personnel_number": TextInput(attrs={"class": "form-control",
                                                 "aria-label": "Здание",
                                                 'placeholder': 'Табельный номер'}),
            "email_user": EmailInput(attrs={"class": "form-control",
                                            "aria-label": "Здание",
                                            'placeholder': 'email'}),
            "days_remaining": TextInput(attrs={"class": "form-control",
                                               "aria-label": "Здание",
                                               'placeholder': 'Количество дней'}),
            "department_user": Select(attrs={"class": "form-select",
                                             "aria-label": "Управление"}),
            "command_number_user": Select(attrs={"class": "form-select",
                                                 "aria-label": "Отдел"}),

        }


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=TextInput(
            attrs={"autofocus": True, "class": "form-control", 'id': 'floatingInput',
                   'placeholder': 'Имя пользователя'}))
    password = CharField(
        label=("Password"),
        strip=False,
        widget=PasswordInput(
            attrs={"autocomplete": "current-password", "class": "form-control", 'id': 'floatingPassword',
                   'placeholder': 'Пароль'}),
    )


class FilterForm(ModelForm):
    class Meta:
        model = UserFilterModel
        exclude = [
            "employee",
            "year_filter",
            "use_department_filter",
            "use_command_number_filter"
        ]
        widgets = {
            "department_filter": Select(attrs={"class": "form-select",
                                               "aria-label": "Управление"}),
            "command_number_filter": Select(attrs={"class": "form-select",
                                                   "aria-label": "Отдел"}),
        }


class YearForm(ModelForm):
    class Meta:
        model = YearModel
        exclude = []
        widgets = {
            "year": Select(attrs={"class": "form-select",
                                  "aria-label": "Год"}),
            }
