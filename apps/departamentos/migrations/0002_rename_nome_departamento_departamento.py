# Generated by Django 3.2.11 on 2022-01-19 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departamento',
            old_name='nome',
            new_name='departamento',
        ),
    ]