from django.db import models

# Create your models here.

PROFILE_TYPES = (
    ("PSP", "Psicopedagogía"),
    ("PSI", "Psicología"),
    ("TO", "Terapia Ocupacional"),
    ("NEU", "Neurolingüista"),
    ("FONO", "Fonoaudiología"),
    ("PROF_ESP", "Prof de Educ Especial")
)

class Person(models.Model):
    # null=True and blank=True -> It's not mandatory, null (db) blank (form)
    name = models.CharField("Nombre", max_length=40)
    location = models.CharField("Localidad", max_length=40, null=True, blank=True)
    address = models.CharField("Dirección", max_length=60, null=True, blank=True)
    phone_number = models.IntegerField("Teléfono", null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

class Diagnostic(models.Model):
    name = models.CharField("Nombre", max_length=60)
    dx_code = models.CharField("Código", max_length=60)

class School(models.Model):
    name = models.CharField("Nombre Escuela", max_length=60)
    school_type = models.CharField("Tipo Escuela", max_length=15)
    location = models.CharField("Localidad", max_length=40)
    address = models.CharField("Dirección", max_length=60)
    contact = models.ForeignKey(Person, on_delete=models.PROTECT, null=True, blank=True)
    phone = models.IntegerField("Teléfono", null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

class Client(models.Model):
    name = models.CharField("Nombre", max_length=40)
    birthday_date = models.DateField("Fecha de Nacimiento")
    age = models.IntegerField("Edad")
    dni_number = models.IntegerField("Número de Documento", null=True, blank=True)
    diagnostic = models.ForeignKey(Diagnostic, on_delete=models.PROTECT, null=True, blank=True)
    location = models.CharField("Localidad", max_length=40)
    phone_number = models.IntegerField("Teléfono", null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    health_insurance_name = models.CharField("Obra social", max_length=10)
    health_insurance_number = models.IntegerField("Número de Afiliado", null=True, blank=True)
    school_level = models.CharField("Nivel", max_length=15)

class Therapist(models.Model):
    name = models.CharField("Nombre", max_length=40)
    location = models.CharField("Localidad", max_length=40)
    phone_number = models.IntegerField("Teléfono")
    email = models.EmailField(null=True, blank=True)
    profile = models.CharField("Ocupación", max_length=10, choices=PROFILE_TYPES, default="PSI")
    has_experience = models.BooleanField("Experiencia")

class Contract(models.Model):
    therapist = models.ForeignKey(Therapist, on_delete=models.PROTECT)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    start_date = models.DateField("Fecha de Inicio")
    contract_type = models.CharField("Tipo", max_length=15)
    school = models.ForeignKey(School, on_delete=models.PROTECT)
    is_active = models.BooleanField("Activo")
    status = models.CharField("Estado", max_length=20)
    obs = models.CharField("Observaciones", max_length=150, null=True, blank=True)


