from django.contrib import admin
from . import models

# Register your models here.

my_models = [
    models.Client,
    models.Contract,
    models.Diagnostic,
    models.Person,
    models.School,
    models.Therapist
]

admin.site.register(my_models)