from django.core import validators
from django import forms
from .models import Blog


class BlogModelForm (forms.ModelForm):
    class Meta:
        model = Blog
        fields= '__all__'

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'category' : forms.Select(attrs={'class': 'form-control'}),
            'author' : forms.TextInput(attrs={'class': 'form-control'}),
            'image_file' : forms.FileInput(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),

            
        }