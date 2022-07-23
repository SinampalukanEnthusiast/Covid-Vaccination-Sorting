from django.contrib import admin
from .models import Districts, NationalIdHolders
# Register your models here.
admin.site.register(Districts)


class IDAdmin(admin.ModelAdmin):
    list_display = ('name', 'district', 'is_vaccinated',
                    'birthday', 'civil_status', 'birthday')


admin.site.register(NationalIdHolders, IDAdmin)
