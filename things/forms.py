"""Forms of the project."""
from django import forms
from .models import Thing
from dataclasses import field, fields

class ThingForm(forms.ModelForm):
    
    class Meta:
        model = Thing
        fields = ["name", "description", "quantity"]
        widgets = {"description": forms.Textarea(), "quantity": forms.NumberInput()}
