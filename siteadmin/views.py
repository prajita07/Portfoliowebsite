from django.shortcuts import render, redirect
from django.http import HttpResponse
from ContactMe.models import ContactMe
from home.forms import  BannerForm
from home.models import  Banner
from AboutMe.models import AboutMe, Skills, Timeline
from AboutMe.forms import SkillsForm, TimelineForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib  import messages 
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect


@login_required
def dashbaord(request):
     return render(request,'dashboard/index.html')


@login_required
def contact(request):
     context={
          'ContactMe': ContactMe.objects.all()
     }    
     return render(request, 'dashboard/contact.html', context)


@login_required
def home_admin(request):
    if request.method == 'GET':
        banners = Banner.objects.all()
        context = {
        'banners': banners,
        }
        return render(request, 'dashboard/home.html', context)


@login_required
def update_homeadmin(request, id=0):
     if request.method == 'GET':
          if id == 0:
               form = BannerForm()
          else:
               addBanner= Banner.objects.get(pk=id)
               form = BannerForm(instance=addBanner)
          return render(request, 'dashboard/home.html', {'form':form})
     else:
          if id == 0:
               form = BannerForm(request.POST, request.FILES)
          else:
               addBanner =Banner.objects.get(pk=id)
               form= BannerForm(request.POST, request.FILES, instance= addBanner)
          if  form.is_valid():
               form.save()
               return redirect('home_admin')


@login_required
def list_aboutadmin(request):
    about = AboutMe.objects.get(id=4)
    timelines = Timeline.objects.all()
    skills = Skills.objects.all()
    tms = []

    for i in range(len(timelines)):
        remainder = i%2
        tms.append([remainder, timelines[i]])


    context ={
        'about': about,
        'timelines': tms,
        'skills': skills
       
    }

    return render(request,'admin/about.html',context)


@login_required
def create_skill(request):
     if request.method == 'GET':
          form = SkillsForm()
          return render(request, 'admin/add_adminabout.html', {'form':form})
     else:
          form = SkillsForm(request.POST or None, request.FILES)
          if form.is_valid():
               form.save()
               return redirect('list_aboutadmin')
          else:
               return redirect('list_aboutadmin')
    
@login_required
def detail_adminabout(request, id):
     if request.method == "GET" :
          skill = Skills.objects.get(id=id)
          context = {
               'skill':skill,
          }
          return render(request,'admin/detail_adminabout.html', context)

@login_required
def admin_delete_about(request, id):
    skill = Skills.objects.get(pk=id)
    skill.delete()
    return redirect('list_aboutadmin')


@login_required
def showthis(request):
     users= User.objects.all()

     context = {'users': users}

     return render(request, 'admin/Users/users.html' , context)


@login_required
def update_adminabout(request, id):
    if request.method == 'GET':
        addSkill = Skills.objects.get(pk = id )
        form = SkillsForm (instance= addSkill)
        return render(request,'admin/add_adminabout.html', {'form':form,'skill':addSkill})
    else:
        addSkill = Skills.objects.get(pk = id )
        form = SkillsForm (request.POST, request.FILES, instance= addSkill)
        if form.is_valid():
            form.save()
        else:
            addSkill.name = request.POST.get('name')
            addSkill.save()
        return redirect('list_aboutadmin')


@login_required
def update_adminExperiences( request, id=0):
     if request.method == 'GET':
          if id == 0:
               form=TimelineForm()
               return render(request, 'admin/add_experience.html', {'form':form})
          else:
               addExperience =Timeline.objects.get(pk=id)
               form = TimelineForm (instance = addExperience)
               return render (request, 'admin/add_experience.html', {'form': form}) 
     else:
          if id == 0:
               form = TimelineForm(request.POST, request.FILES)
          else:
               addExperience = Timeline.objects.get(pk=id)
               form = TimelineForm(request.POST, request.FILES, instance= addExperience)
          if form.is_valid():
               form.save()
          return redirect('list_aboutadmin')

@login_required
def change_password(request):
     if request.method == 'POST':
          form = PasswordChangeForm(request.user, request.POST)
          if form.is_valid():
               user = form.save()
               update_session_auth_hash(request, users)
               message.sucess(request, 'your password was sucessfully updated!')
               return redirect ('dashboard')
          else:
               message.error(request, 'Please correct the error below.')
     else:
          form = PasswordChangeForm(request.user)
     return render(request, 'admin/users/change_password.html', {'form':form}) 





