from .models import VacationsModel, EmployeeModel
from django.forms import ModelForm, Select, SelectDateWidget, DateInput, TextInput
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
                                                     "aria-label": "Здание"}),
            "middle_name": TextInput(attrs={"class": "form-control",
                                                     "aria-label": "Здание"}),
            "last_name": TextInput(attrs={"class": "form-control",
                                                     "aria-label": "Здание"}),

        }