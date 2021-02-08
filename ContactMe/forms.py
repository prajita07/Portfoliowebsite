from django import forms
from .models import ContactMe

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactMe
        fields = '__all__'

        # exclude= ('received_at',)