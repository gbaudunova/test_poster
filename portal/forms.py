from django import forms
from .models import Portal


class PortalForm(forms.ModelForm):
    login = forms.CharField(max_length=120)
    password = forms.CharField(max_length=120)
    
    class Meta:
        model = Portal
        fields = ('name', 'user')
        widgets = {'name': forms.HiddenInput(), 'user': forms.HiddenInput()}
