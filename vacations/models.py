from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class EmployeeModel(models.Model):
    last_name = models.CharField("Фамилия", max_length=150)
    first_name = models.CharField("Имя", max_length=150)
    middle_name = models.CharField("Отчество", max_length=150)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    class Meta:
        verbose_name = _("сотрудник")
        verbose_name_plural = _("сотрудники")


class VacationsModel(models.Model):
    employee = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE, verbose_name="Сотрудник")
    vacation_start = models.DateField(verbose_name="Начало отпуска")
    vacation_end = models.DateField(verbose_name="Окончание отпуска")

    def __str__(self):
        return f'{self.employee}: {self.vacation_start} {self.vacation_end}'

    class Meta:
        verbose_name = _("отпуск")
        verbose_name_plural = _("отпуска")
