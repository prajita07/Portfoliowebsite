from django.shortcuts import render, redirect
from project.models import Project, ProjectCategory
from project.forms import ProjectModelForm


def list_adminproject(request):
     if request.method =='GET':  
        projects = Project.objects.all()
        new_projects = Project.objects.all().order_by('-created_at')
        context = {   
          'projects' : projects,
          'new_projects' : new_projects,
          'categories': ProjectCategory.objects.all()
          }
        return render(request, 'admin/admin_project/admin_project.html', context)
     else:
      projects = Project.objects.filter(category__id=request.POST.get('project-category'))
      context  = {
          'filtered_projects': projects,
          'categories': ProjectCategory.objects.all(),
          'projectcat': ProjectCategory.objects.get(id=request.POST.get('project-category'))
       }
     return render(request, 'admin/admin_project/admin_project.html', context)
def add_adminproject(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ProjectModelForm()
        else:
            addProject = Project.objects.get(pk=id)
            form = ProjectModelForm(instance=addProject)
        return render(request,"admin/admin_project/add_adminproject.html", {'form':form})
    else:
        if id == 0:
            form = ProjectModelForm(request.POST, request.FILES)
        else:
            addProject = Project.objects.get(pk=id)
            form = ProjectModelForm(request.POST,request.FILES, instance = addProject)
        if form.is_valid():
            form.save()
        return redirect('list_adminproject')


def search_adminproject(request):
      if request.method == 'POST':
            projects = Project.objects.filter(title__icontains=request.POST.get('search'))
            context ={
                'results':projects,
                'search':request.POST.get('search')
              }
            return render(request, 'admin/admin_project/admin_project.html', context)
      return redirect('list_adminproject')

def detail_admin_project(request, id):
  if request.method == "GET" :
    project = Project.objects.get(id=id)
    context = {
      'project' : project,
    }
    return render(request,'admin/admin_project/detail_project.html', context)

def admin_delete_project(request, id):
    project = Project.objects.get(pk=id)
    project.delete()
    return redirect('list_adminproject')