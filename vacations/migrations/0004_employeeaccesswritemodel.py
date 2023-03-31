# Generated by Django 4.1.7 on 2023-03-31 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacations', '0003_employeemodel_days_remaining'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeAccessWriteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('write_permission', models.BooleanField(default=False, verbose_name='Право записи')),
                ('access_level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vacations.accesslevelmodel', verbose_name='Вид доступа')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacations.employeemodel', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'право сотрудника',
                'verbose_name_plural': 'права сотрудников',
            },
        ),
    ]
