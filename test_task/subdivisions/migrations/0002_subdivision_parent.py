# Generated by Django 3.1.5 on 2021-02-20 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subdivisions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subdivision',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='subdivisions.subdivision', verbose_name='Подчиненность'),
        ),
    ]