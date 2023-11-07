from django.shortcuts import render, get_object_or_404
from .models import Project

def all_projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }

    return render(request, 'projects/projects.html', context)

def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    context = {
        'project': project
    }

    return render(request, 'projects/project_detail.html', context)