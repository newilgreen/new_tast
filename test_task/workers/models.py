from django.db import models
from datetime import date
from users.models import CustomUser
from subdivisions.models import Subdivision


class Worker(models.Model):
    """Работник"""
    name = models.CharField("Фио работника", max_length=150)
    user_name = models.OneToOneField(
        CustomUser, verbose_name="Работник", on_delete=models.SET_NULL, null=True, related_name="castomuser"
    )
    subdivision = models.OneToOneField(
        Subdivision, verbose_name="Подразделение", on_delete=models.SET_NULL, null=True, related_name="subdivision"
    )
    position = models.CharField("Должность", max_length=100)
    salary = models.PositiveSmallIntegerField("Ставка", default=0, help_text='Ставка указывается в рублях')
    recruitment_date = models.DateField("Дата приема на работу", default=date.today)
    dismissal_point = models.BooleanField("Находится в штате", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"


class Dismissal_list(models.Model):
    """Увольнение"""
    worker_name = models.ForeignKey(
        Worker, verbose_name="Фио работника", on_delete=models.SET_NULL, null=True, related_name="worker"
    )
    dismissal_date = models.DateField("Дата увольнения", default=date.today)
    dismissal = models.CharField("Приказ об увольнении", max_length=8)

    def __str__(self):
        return self.dismissal

    class Meta:
        verbose_name = "Увольнение"
        verbose_name_plural = "Увольнения"
