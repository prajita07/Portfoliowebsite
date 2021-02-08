from django.core import validators
from django import forms
from .models import Project


class ProjectModelForm (forms.ModelForm):
    class Meta: 
        model = Project
        fields= '__all__'

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'category' : forms.Select(attrs={'class': 'form-control'}),
            'author' : forms.TextInput(attrs={'class': 'form-control'}),
            'image_file' : forms.FileInput(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),

            
        }