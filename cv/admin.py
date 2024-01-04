from django.contrib import admin
from .models import ProfessionalExperience

class ProfessionalAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'company',
        'location',
        'start_date',
        'end_date'
    )

    ordering = ('end_date',)

admin.site.register(ProfessionalExperience, ProfessionalAdmin)

