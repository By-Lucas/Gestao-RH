# Generated by Django 4.0.4 on 2022-05-19 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0009_alter_funcionario_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='foto_funcionatio',
            field=models.ImageField(blank=True, null=True, upload_to=models.CharField(help_text='Nome do funcionário', max_length=100)),
        ),
    ]
