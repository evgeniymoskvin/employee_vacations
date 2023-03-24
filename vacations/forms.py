from .models import VacationsModel, EmployeeModel
from django.forms import ModelForm, Select, SelectDateWidget, DateInput, TextInput, CharField, PasswordInput
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.admin.widgets import AdminDateWidget


class DateInputCustom(DateInput):
    input_type = 'date'


class AddVacationForm(ModelForm):
    class Meta:
        model = VacationsModel
        fields = '__all__'

        widgets = {"employee": Select(attrs={"class": "form-select",
                                             "aria-label": "Сотрудник"}),
                   "vacation_start": DateInputCustom(attrs={"class": "form-control"}),
                   "vacation_end": DateInputCustom(attrs={"class": "form-control"}),

                   }


class AddEmployeeForm(ModelForm):
    class Meta:
        model = EmployeeModel
        fields = "__all__"

        widgets = {
            "first_name": TextInput(attrs={"class": "form-control",
                                           "aria-label": "Здание",
                                           'placeholder': 'Имя'}),
            "middle_name": TextInput(attrs={"class": "form-control",
                                            "aria-label": "Здание",
                                           'placeholder': 'Отчество'}),
            "last_name": TextInput(attrs={"class": "form-control",
                                          "aria-label": "Здание",
                                           'placeholder': 'Фамилия'})

        }


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=TextInput(
            attrs={"autofocus": True, "class": "form-control", 'id': 'floatingInput', 'placeholder': 'Имя пользователя'}))
    password = CharField(
        label=("Password"),
        strip=False,
        widget=PasswordInput(
            attrs={"autocomplete": "current-password", "class": "form-control", 'id': 'floatingPassword',
                   'placeholder': 'Пароль'}),
    )
