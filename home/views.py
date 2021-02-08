from django.shortcuts import render, redirect
from .forms import SubscribeForm, BannerForm
from .models import Subscription, Banner
from project.models import Project
from blog.models import Blog

def home(request):
    banners = Banner.objects.all()

    context = {
        'banners': banners,
        'blogs': Blog.objects.filter(is_popular=True),
        'projects': Project.objects.filter(is_popular=True)
    }
    return render(request, 'home.html', context)

def subscribe_form(request, id=0):
    if request.method == "POST":
        form = SubscribeForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        return redirect('home')

