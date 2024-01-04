from django.shortcuts import render
from .models import ProfessionalExperience, AcademicExperience

def cv(request):
    professional_exp = ProfessionalExperience.objects.all()
    academic_exp = AcademicExperience.objects.all()
    context = {
        'professional_exp': professional_exp,
        'academic_exp': academic_exp,
    }

    return render(request, 'cv/cv.html', context)
