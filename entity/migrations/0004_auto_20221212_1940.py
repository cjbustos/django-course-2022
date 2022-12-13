# Generated by Django 3.2 on 2022-12-12 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0003_alter_therapist_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='health_insurance_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Número de Afiliado'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='school',
            name='phone',
            field=models.IntegerField(blank=True, null=True, verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='therapist',
            name='phone_number',
            field=models.IntegerField(verbose_name='Teléfono'),
        ),
    ]