from django import forms
from django.db import models
from django import forms
from core.models import Core


class CoreForm(forms.ModelForm):
    class Meta:
        model = Core 
        fields = ['content', ]