from django.shortcuts import render, redirect
from .models import AboutMe, Skills, Timeline
from .forms import SkillsForm

def list_about(request):
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

    return render(request,'about/about.html',context)

def Skills_form(request, id=0):
    if request.method == "POST":
        form = SkillsForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('AboutMe')
    else:
        return redirect('AboutMe')