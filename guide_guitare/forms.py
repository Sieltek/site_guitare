from django.forms import forms
from .models import GuitareModel

class GuitareForm(forms.Form):
    class Meta:
        model = GuitareModel
        fields = '__all__'
