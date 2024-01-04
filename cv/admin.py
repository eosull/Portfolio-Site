from django.contrib import admin
from .models import ProfessionalExperience, AcademicExperience

class ProfessionalAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'company',
        'location',
        'start_date',
        'end_date'
    )

    ordering = ('end_date',)
class AcademicAdmin(admin.ModelAdmin):
    list_display = (
        'level',
        'institution',
        'start_date',
        'end_date'
    )

    ordering = ('end_date',)

admin.site.register(ProfessionalExperience, ProfessionalAdmin)
admin.site.register(AcademicExperience, AcademicAdmin)
