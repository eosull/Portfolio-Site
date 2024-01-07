from django.shortcuts import render
from portfolio.models import Project
from cv.models import ProfessionalExperience, AcademicExperience, Personal

def home(request):
    # View returning index page
    projects = Project.objects.order_by('-date')[:3]
    prof_exp = ProfessionalExperience.objects.all()
    acad_exp = AcademicExperience.objects.all()
    personal = Personal.objects.get(name="Eoin O'Sullivan")

    context = {
        'projects': projects,
        'prof_exp': prof_exp,
        'acad_exp': acad_exp,
        'personal': personal,
    }

    return render(request, 'home/index.html', context)