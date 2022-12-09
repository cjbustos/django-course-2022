from django import forms

# Here, load parents classes for hierarchy
# A class for a resource

class TherapistForm(forms.Form):
    id = forms.IntegerField(label="Id")
    name = forms.CharField(label="Name", max_length=120)
    profile = forms.CharField(label="Profile")
    experience = forms.IntegerField(label="Experience")
    address = forms.CharField(label="Address", max_length=50)


