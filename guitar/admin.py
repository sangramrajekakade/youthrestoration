from django.contrib import admin

from .models import *
from django.apps import AppConfig

# Register your models here.
admin.site.register(Appointment)
# admin.site.register(AboutGuitar)
# admin.site.register(Batches)
# admin.site.register(Feestructure)
# admin.site.register(Buyguitar)
admin.site.register(Post)
admin.site.register(Offers)





class AppointmentInline(admin.TabularInline):
    model = Appointment

class AppointmentAdmin(admin.ModelAdmin):
    inlines = [
        AppointmentInline,
    ]