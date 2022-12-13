# Generated by Django 3.2 on 2022-12-11 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0002_rename_dx_client_diagnostic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='therapist',
            name='profile',
            field=models.CharField(choices=[('PSP', 'Psicopedagogía'), ('PSI', 'Psicología'), ('TO', 'Terapia Ocupacional'), ('NEU', 'Neurolingüista'), ('FONO', 'Fonoaudiología'), ('PROF_ESP', 'Prof de Educ Especial')], default='PSI', max_length=10, verbose_name='Ocupación'),
        ),
    ]
