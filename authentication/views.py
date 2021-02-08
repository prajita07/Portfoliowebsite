from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


def signupuser(request):
    if request.method == 'GET':
        return render(request,'admin/users/signup.html', {'form': UserCreationForm()} )
    else:
        if request.POST['password1'] == request.POST ['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password= request.POST['password1'])
                user.is_superuser=True
                user.save()
                login(request,user)
                return redirect('loginuser')
            except IntegrityError:
                return render(request,'admin/users/signup.html', {'form': UserCreationForm(), 'error': 'That username has already been taken.Please choose a new username.'} )
        else:
            return render(request,'admin/users/signup.html', {'form': UserCreationForm(), 'error': 'Passwords did not match'} )


def loginuser(request):
    if request.method == 'GET':
        return render(request,'admin/users/login.html', {'form': AuthenticationForm()} )
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        print(f"user: {user}")
        print(request.POST["username"])
        if user is None:
            return render(request,'admin/users/login.html', {'form': AuthenticationForm(), 'error':'username and password did not match'} )
        else:
            login(request,user)
            return redirect('dashboard')


def logoutuser(request):
    if request.method == 'GET':
        logout(request)
        return redirect('loginuser')
    else:
        return redirect('dashboard')