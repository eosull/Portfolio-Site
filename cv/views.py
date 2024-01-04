from django.shortcuts import render
from .models import ProfessionalExperience, AcademicExperience, Personal, Links

def cv(request):
    professional_exp = ProfessionalExperience.objects.all()
    academic_exp = AcademicExperience.objects.all()
    personal = Personal.objects.all()
    links = Links.objects.all()
    context = {
        'professional_exp': professional_exp,
        'academic_exp': academic_exp,
        'personal': personal,
        'links': links,
    }

    return render(request, 'cv/cv.html', context)
