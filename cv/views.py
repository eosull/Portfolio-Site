from django.shortcuts import render
from .models import ProfessionalExperience

def cv(request):
    professional_exp = ProfessionalExperience.objects.all()
    context = {
        'professional_exp': professional_exp,
    }

    return render(request, 'cv/cv.html', context)
