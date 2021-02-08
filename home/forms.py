from django import forms
from .models import Subscription, Banner
class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = '__all__'
class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = '__all__'