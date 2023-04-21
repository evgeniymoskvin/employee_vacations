from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils.translation import gettext_lazy as _
import datetime


# Create your models here.

class JobTitleModel(models.Model):
    """ Таблица должностей """

    job_title = models.CharField("Должность", max_length=200)

    class Meta:
        verbose_name = _("должность")
        verbose_name_plural = _("должности")

    def __str__(self):
        return f'{self.job_title}'


class DepartmentModel(models.Model):
    """Список управлений"""
    department_abr = models.CharField("Сокращенное название управления", max_length=10)
    department_name = models.CharField("Полное название управления", max_length=250)

    def __str__(self):
        return f'{self.department_abr}, {self.department_name}'

    class Meta:
        verbose_name = _("управление")
        verbose_name_plural = _("управления")


class CommandNumberModel(models.Model):
    """Номера отделов"""
    command_number = models.IntegerField("Номер отдела/Сокращение")
    command_name = models.CharField("Наименование отдела", max_length=150)
    department = models.ForeignKey(DepartmentModel, verbose_name="Управление", on_delete=models.SET_NULL, null=True,
                                   blank=True)

    def __str__(self):
        return f'{self.command_number}, {self.command_name}'

    class Meta:
        verbose_name = _("номер отдела")
        verbose_name_plural = _("номера отделов")


class VacationTypeModel(models.Model):
    """Вид отпуска"""
    vacation_type_abr = models.CharField("Сокращенное название вида отпуска", max_length=10)
    vacation_type_name = models.CharField("Полное название вида отпуска", max_length=150)

    def __str__(self):
        return f'{self.vacation_type_abr} - {self.vacation_type_name}'

    class Meta:
        verbose_name = _("вид отпуска")
        verbose_name_plural = _("виды отпусков")


class AccessLevelModel(models.Model):
    """Уровень доступа"""
    access_level = models.CharField("Наименование доступа", max_length=50)

    def __str__(self):
        return f'{self.id} - {self.access_level}'

    class Meta:
        verbose_name = _("уровень доступа")
        verbose_name_plural = _("уровни доступа")


class WritePermissionModel(models.Model):
    """Право записи"""
    write_permission = models.CharField("Наименования права записи", max_length=25)

    def __str__(self):
        return f'{self.id} - {self.write_permission}'

    class Meta:
        verbose_name = _("право записи")
        verbose_name_plural = _("права записи")


class EmployeeModel(models.Model):
    """Таблица сотрудников"""
    user = models.OneToOneField(User, models.PROTECT, verbose_name="Login", null=True, blank=True)
    personnel_number = models.CharField("Табельный номер", max_length=20, null=True)
    last_name = models.CharField("Фамилия", max_length=150)
    first_name = models.CharField("Имя", max_length=150)
    middle_name = models.CharField("Отчество", max_length=150)
    department_user = models.ForeignKey(DepartmentModel, models.SET_NULL, verbose_name="Управление", null=True)
    command_number_user = models.ForeignKey(CommandNumberModel, models.SET_NULL, verbose_name="Отдел", null=True)
    email_user = models.EmailField(verbose_name="Email", null=True, blank=True)
    show_employee = models.BooleanField(verbose_name="Отображать сотрудника", default=True)
    days_remaining = models.IntegerField(verbose_name="Количество неиспользованных дней", default=0)

    # show_year = models.IntegerField(verbose_name="Отображаемый год", default=datetime.datetime.today().year)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    class Meta:
        verbose_name = _("сотрудник")
        verbose_name_plural = _("сотрудники")


class VacationsModel(models.Model):
    """Таблица отпусков"""
    employee = models.ForeignKey(EmployeeModel, on_delete=models.PROTECT, verbose_name="Сотрудник")
    vacation_start = models.DateField(verbose_name="Начало отпуска")
    day_count = models.IntegerField(verbose_name="Количество дней", null=True)
    vacation_end = models.DateField(verbose_name="Окончание отпуска", null=True, blank=True)
    vacation_type = models.ForeignKey(VacationTypeModel, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f'{self.employee}: {self.vacation_start} {self.vacation_end} '

    class Meta:
        verbose_name = _("отпуск")
        verbose_name_plural = _("отпуска")

    def save(self, *args, **kwargs):
        self.vacation_end = self.vacation_start + datetime.timedelta(days=(self.day_count - 1))
        super(VacationsModel, self).save(*args, **kwargs)


class EmployeeAccessWriteModel(models.Model):
    """Таблица прав доступа и записи каждого сотрудника"""
    employee = models.OneToOneField(EmployeeModel, on_delete=models.CASCADE, verbose_name="Сотрудник")
    access_level = models.ForeignKey(AccessLevelModel, on_delete=models.SET_NULL, null=True, verbose_name="Вид доступа")
    write_permission = models.BooleanField(verbose_name="Право записи", default=False)

    def __str__(self):
        return f'{self.employee}. Доступ - {self.access_level}. Право записи - {self.write_permission}'

    class Meta:
        verbose_name = _("право сотрудника")
        verbose_name_plural = _("права сотрудников")


class UserFilterModel(models.Model):
    """Таблица фильтрации записей для каждого пользователя"""
    employee = models.OneToOneField(EmployeeModel, on_delete=models.CASCADE, verbose_name="Сотрудник")
    year_filter = models.IntegerField(verbose_name="Год", blank=True, null=True)
    department_filter = models.ForeignKey(DepartmentModel, verbose_name="Управление", blank=True, null=True,
                                          on_delete=models.CASCADE)
    command_number_filter = models.ForeignKey(CommandNumberModel, verbose_name="Отдел", blank=True, null=True,
                                              on_delete=models.CASCADE)
    use_department_filter = models.BooleanField(verbose_name="Фильтр управления включен", blank=True, default=False)
    use_command_number_filter = models.BooleanField(verbose_name="Фильтр управления включен", blank=True, default=False)

    def __str__(self):
        return f'{self.employee}. Фильтры: {self.year_filter}, {self.department_filter}, {self.command_number_filter}'

    class Meta:
        verbose_name = _("фильтр сотрудника")
        verbose_name_plural = _("фильтры сотрудников")


class YearModel(models.Model):
    """Таблица годов для выпадающего списка"""
    year = models.IntegerField(verbose_name="год")

    def __str__(self):
        return f'{self.year}'

    class Meta:
        verbose_name = _("год")
        verbose_name_plural = _("года")


class LogModel(models.Model):
    employee = models.CharField(verbose_name="Имя пользователя", null=True, blank=True, max_length=150)
    id_vacation = models.IntegerField(verbose_name="Id записи")
    action = models.CharField(verbose_name="Действие", max_length=20)
    old_vacation_start = models.DateField(verbose_name="Начало отпуска (old)", null=True, blank=True)
    old_vacation_end = models.DateField(verbose_name="Окончание отпуска (old)", null=True, blank=True)
    new_vacation_start = models.DateField(verbose_name="Начало отпуска (new)")
    new_vacation_end = models.DateField(verbose_name="Окончание отпуска (new)", null=True, blank=True)
    datetime_edit = models.DateField(verbose_name="Дата изменения", auto_now_add=True)

    def __str__(self):
        return f'{self.datetime_edit} Пользователь {self.employee} {self.action} запись {self.id_vacation}: ' \
               f'Было {self.old_vacation_start} - {self.old_vacation_end}.' \
               f'Стало: {self.new_vacation_start} - {self.new_vacation_end}'



