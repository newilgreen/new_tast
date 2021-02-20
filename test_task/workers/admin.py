from django.contrib import admin

from workers.models import Worker, Dismissal_list

admin.site.register(Worker)
admin.site.register(Dismissal_list)

# Register your models here.
