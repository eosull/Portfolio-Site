from django.shortcuts import render
from portfolio.views import Project

def home(request):
    # View returning index page
    projects = Project.objects.order_by('-date')[:2]

    context = {
        'projects': projects,
    }

    return render(request, 'home/index.html', context)