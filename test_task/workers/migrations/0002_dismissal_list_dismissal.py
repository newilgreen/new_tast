# Generated by Django 3.1.5 on 2021-02-19 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dismissal_list',
            name='dismissal',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Приказ об увольнении'),
        ),
    ]