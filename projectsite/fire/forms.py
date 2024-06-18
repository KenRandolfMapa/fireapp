from django import forms
from .models import FireStation, Incident

class FireStationForm(forms.ModelForm):
    class Meta:
        model = FireStation
        fields = ['name', 'latitude', 'longitude', 'address', 'city', 'country']

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = "__all__"
