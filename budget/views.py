from django.shortcuts import render, get_object_or_404
from .models import Project

def project_list(request):
    return render(request, 'budget/product_list.html', {})

def project_detail(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    return render(request, 'budget/project_detail.html', {'project': project})
