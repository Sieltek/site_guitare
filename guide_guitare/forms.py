from django import forms
from .models import GuitareModel


class GuitareForm(forms.ModelForm):
    class Meta:
        model = GuitareModel
        fields = '__all__'
        widgets = {
            'nom_guitare': forms.TextInput(attrs={'class': 'form-control'}),
            'type_guitare': forms.Select(attrs={'class': 'form-control'}),
            'description_guitare': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'prix_guitare': forms.NumberInput(attrs={'class': 'form-control'}),
            'photo_guitare': forms.ClearableFileInput(attrs={'class': 'custom-file'}),
            'user_guitare': forms.Select(attrs={'class': 'custom-file'}),
        }
        labels = {

        }
