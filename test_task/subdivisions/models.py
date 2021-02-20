from django.db import models


class Subdivision(models.Model):
    """Подразделение"""
    name = models.CharField("Название подразделения", max_length=150)
    abbreviation = models.CharField("Аббревиатура", max_length=15)
    parent = models.ForeignKey('self', verbose_name="Подчиненность", on_delete=models.SET_NULL, blank=True, null=True, related_name="children")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подразделение"
        verbose_name_plural = "Подразделения"


