from django.forms import ModelForm
from  django import forms
from .models import workout_model

class workout_forms(forms.ModelForm):
    class Meta():
        model=workout_model
        fields='__all__'
class workout_froms_f(forms.Form):
    calories=forms.CharField()
