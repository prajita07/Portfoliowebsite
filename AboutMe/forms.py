from django import forms
from .models import Skills, Timeline
class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'
class TimelineForm(forms.ModelForm):
    class Meta:
        model = Timeline
        fields = '__all__'
    