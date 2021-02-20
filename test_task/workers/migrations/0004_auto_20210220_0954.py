# Generated by Django 3.1.5 on 2021-02-20 06:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subdivisions', '0002_subdivision_parent'),
        ('workers', '0003_auto_20210219_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dismissal_list',
            name='worker_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='worker', to='workers.worker', verbose_name='Фио работника'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='subdivision',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subdivision', to='subdivisions.subdivision', verbose_name='Подразделение'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='user_name',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='castomuser', to=settings.AUTH_USER_MODEL, verbose_name='Работник'),
        ),
    ]
