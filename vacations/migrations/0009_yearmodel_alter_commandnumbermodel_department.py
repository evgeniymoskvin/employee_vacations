# Generated by Django 4.1.7 on 2023-04-04 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacations', '0008_commandnumbermodel_department'),
    ]

    operations = [
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
        migrations.AlterField(
            model_name='commandnumbermodel',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vacations.departmentmodel', verbose_name='Управление'),
        ),
    ]