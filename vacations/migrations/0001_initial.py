# Generated by Django 4.1.7 on 2023-06-13 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommandNumberModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command_number', models.IntegerField(verbose_name='Номер отдела/Сокращение')),
                ('command_name', models.CharField(max_length=150, verbose_name='Наименование отдела')),
            ],
            options={
                'verbose_name': 'номер отдела',
                'verbose_name_plural': 'номера отделов',
                'db_table': 'ToDo_tasks_commandnumbermodel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=150, verbose_name='Имя')),
                ('middle_name', models.CharField(max_length=150, verbose_name='Отчество')),
                ('personnel_number', models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='Табельный номер')),
                ('user_phone', models.IntegerField(default=None, null=True, verbose_name='№ телефона')),
                ('right_to_sign', models.BooleanField(default=False, verbose_name='Право подписывать')),
                ('check_edit', models.BooleanField(default=True, verbose_name='Возможность редактирования')),
                ('can_make_task', models.BooleanField(default=True, verbose_name='Возможность выдавать задания')),
                ('cpe_flag', models.BooleanField(default=False, verbose_name='Флаг ГИП (техническая метка)')),
                ('mailing_list_check', models.BooleanField(default=True, verbose_name='Получать рассылку')),
                ('work_status', models.BooleanField(default=True, verbose_name='Сотрудник работает')),
            ],
            options={
                'verbose_name': 'сотрудник',
                'verbose_name_plural': 'сотрудники',
                'db_table': 'ToDo_tasks_employee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GroupDepartmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_dep_abr', models.CharField(max_length=10, verbose_name='Сокращенное название управления')),
                ('group_dep_name', models.CharField(max_length=250, verbose_name='Полное название управления')),
            ],
            options={
                'verbose_name': 'управление',
                'verbose_name_plural': 'управления',
                'db_table': 'ToDo_tasks_groupdepartmentmodel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='JobTitleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=200, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'должность',
                'verbose_name_plural': 'должности',
                'db_table': 'ToDo_tasks_jobtitlemodel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AccessLevelModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_level', models.CharField(max_length=50, verbose_name='Наименование доступа')),
            ],
            options={
                'verbose_name': 'уровень доступа',
                'verbose_name_plural': 'уровни доступа',
            },
        ),
        migrations.CreateModel(
            name='LogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.CharField(blank=True, max_length=150, null=True, verbose_name='Имя пользователя')),
                ('id_vacation', models.IntegerField(verbose_name='Id записи')),
                ('action', models.CharField(max_length=20, verbose_name='Действие')),
                ('old_vacation_start', models.DateField(blank=True, null=True, verbose_name='Начало отпуска (old)')),
                ('old_vacation_end', models.DateField(blank=True, null=True, verbose_name='Окончание отпуска (old)')),
                ('new_vacation_start', models.DateField(verbose_name='Начало отпуска (new)')),
            ],
        ),
        migrations.CreateModel(
            name='VacationTypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacation_type_abr', models.CharField(max_length=10, verbose_name='Сокращенное название вида отпуска')),
                ('vacation_type_name', models.CharField(max_length=150, verbose_name='Полное название вида отпуска')),
            ],
            options={
                'verbose_name': 'вид отпуска',
                'verbose_name_plural': 'виды отпусков',
            },
        ),
        migrations.CreateModel(
            name='WritePermissionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('write_permission', models.CharField(max_length=25, verbose_name='Наименования права записи')),
            ],
            options={
                'verbose_name': 'право записи',
                'verbose_name_plural': 'права записи',
            },
        ),
        migrations.CreateModel(
            name='YearModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='год')),
            ],
            options={
                'verbose_name': 'год',
                'verbose_name_plural': 'года',
            },
        ),
        migrations.CreateModel(
            name='VacationsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacation_start', models.DateField(verbose_name='Начало отпуска')),
                ('day_count', models.IntegerField(null=True, verbose_name='Количество дней')),
                ('vacation_end', models.DateField(blank=True, null=True, verbose_name='Окончание отпуска')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vacations.employeemodel', verbose_name='Сотрудник')),
                ('vacation_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='vacations.vacationtypemodel')),
            ],
            options={
                'verbose_name': 'отпуск',
                'verbose_name_plural': 'отпуска',
            },
        ),
        migrations.CreateModel(
            name='UserFilterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_filter', models.IntegerField(blank=True, null=True, verbose_name='Год')),
                ('use_department_filter', models.BooleanField(blank=True, default=False, verbose_name='Фильтр управления включен')),
                ('use_command_number_filter', models.BooleanField(blank=True, default=False, verbose_name='Фильтр управления включен')),
                ('command_number_filter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vacations.commandnumbermodel', verbose_name='Отдел')),
                ('department_filter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vacations.groupdepartmentmodel', verbose_name='Управление')),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='vacations.employeemodel', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'фильтр сотрудника',
                'verbose_name_plural': 'фильтры сотрудников',
            },
        ),
        migrations.CreateModel(
            name='RemainingDaysModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days_remaining', models.IntegerField(default=0, verbose_name='Количество неиспользованных дней')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vacations.employeemodel', verbose_name='Сотрудник')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeAccessWriteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('write_permission', models.BooleanField(default=False, verbose_name='Право записи')),
                ('access_level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vacations.accesslevelmodel', verbose_name='Вид доступа')),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='vacations.employeemodel', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'право сотрудника',
                'verbose_name_plural': 'права сотрудников',
            },
        ),
    ]
