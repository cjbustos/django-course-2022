from django import forms

# Work with models add
from django.forms import ModelForm
from .models import Diagnostic, Client

# Here, load parents classes for hierarchy
# Only write a class for unique resource, in this case "TherapistForm.class"

class TherapistForm(forms.Form):
    id = forms.IntegerField(label="Id")
    name = forms.CharField(label="Name", max_length=120)
    PROFILE_TYPE = (
        (1, "psicologia"),
        (2, "psicopedagogia"),
        (3, "fonoaudiologia"),
        (4, "terapia ocupacional")
    )
    profile = forms.ChoiceField(label="Profile", choices=PROFILE_TYPE)
    #experience = forms.IntegerField(label="Experience", required=False)
    experience = forms.BooleanField(label="Experience", required=False)
    address = forms.CharField(label="Address", max_length=50)

    # Date types options
    # date_have_to_degree = forms.DateField(label="Año de egreso", input_formats=["%d/%m/%Y"])
    # date_have_to_degree = forms.DateField(label="Año de egreso", widget=forms.DateInput(attrs={"type": "date"}))

# class DiagnosticForm(forms.Form):
#     name = forms.CharField(label="Nombre")
#     dx_code = forms.CharField(label="Código")

# DiagnosticForm refactor - Rewrite form when come back to the models
class DiagnosticForm(ModelForm):
    class Meta:
        model = Diagnostic
        fields = '__all__'

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'