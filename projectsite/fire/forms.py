from django import forms
from .models import FireStation, Locations, Incident, Firefighters

class FireStationForm(forms.ModelForm):
    class Meta:
        model = FireStation
        fields = ['name', 'latitude', 'longitude', 'address', 'city', 'country']

class LocationsForm(forms.ModelForm):
    class Meta:
        model = Locations
        fields = "__all__"

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = "__all__"
        
class FirefightersForm(forms.ModelForm):
    class Meta:
        model = Firefighters
        fields = ['name', 'rank', 'experience_level', 'station']