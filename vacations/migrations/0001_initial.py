# Generated by Django 4.1.7 on 2023-03-20 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=150, verbose_name='Имя')),
                ('middle_name', models.CharField(max_length=150, verbose_name='Отчество')),
            ],
            options={
                'verbose_name': 'сотрудник',
                'verbose_name_plural': 'сотрудники',
            },
        ),
        migrations.CreateModel(
            name='VacationsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacation_start', models.DateField()),
                ('vacation_end', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacations.employeemodel', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'отпуск',
                'verbose_name_plural': 'отпуска',
            },
        ),
    ]
