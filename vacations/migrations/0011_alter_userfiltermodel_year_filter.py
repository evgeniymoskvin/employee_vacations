# Generated by Django 4.1.7 on 2023-04-04 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacations', '0010_alter_userfiltermodel_year_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfiltermodel',
            name='year_filter',
            field=models.IntegerField(blank=True, null=True, verbose_name='Год'),
        ),
    ]