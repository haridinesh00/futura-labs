from django.contrib import admin

from app import models

# Register your models here.
admin.site.register(models.Login)
# admin.site.register(models.Customer)
# admin.site.register(models.Worker)
admin.site.register(models.Feedback)
admin.site.register(models.WorkerCategory)
admin.site.register(models.WorkSchedule)
admin.site.register(models.BookAppointment)
admin.site.register(models.Bill)
