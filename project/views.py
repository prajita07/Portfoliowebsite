from django.shortcuts import render, redirect
from .models import Project, ProjectCategory
from .forms import ProjectModelForm


def list_project(request):
     if request.method =='GET':  
        projects = Project.objects.all()
        new_projects = Project.objects.all().order_by('-created_at')
        context = {   
          'projects' : projects,
          'new_projects' : new_projects,
          'categories': ProjectCategory.objects.all()
          }
        return render(request, 'project/project.html', context)
     else:
      projects = Project.objects.filter(category__id=request.POST.get('project-category'))
      context  = {
          'filtered_projects': projects,
          'categories': ProjectCategory.objects.all(),
          'projectcat': ProjectCategory.objects.get(id=request.POST.get('project-category'))
       }
     return render(request, 'project/project.html', context)
def add_project(request):
    if request.method == 'POST':
     form= ProjectModelForm(request.POST, request.FILES)
     if form.is_valid():
       form.save()
       return redirect('list_project')
    else:
      form= ProjectModelForm()
     
    return render (request, 'project/add_project.html', {'form':form})

def search_project(request):
    if request.method == 'POST':
        projects = Project.objects.filter(title__icontains=request.POST.get('search'))
        # new_projects = Project.objects.filter(title__icontains = request.POST.get('search'))
        context ={
          'projects':projects,
          'search':request.POST.get('search')
        # 'new_projects': new_projects
        }
        return redirect('list_project')
    return redirect('list_project')