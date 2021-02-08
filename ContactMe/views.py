from django.shortcuts import render, redirect
from .models import ContactMe
from .forms import ContactModelForm

def list_contact(request):
    if request.method=="POST":
        form = ContactModelForm(request.POST or None)
        if form.is_valid():
            form.save()
            # form = ContactModelForm()
            # context = {
            #     'form':form
            # }
            # return render(request, 'contact/contact.html')
            return redirect('list_contact')
        else:
            redirect('list_contact')

    else:
        form = ContactModelForm()
        context = {
            'form':form
        }
        return render(request, 'contact/contact.html', context)