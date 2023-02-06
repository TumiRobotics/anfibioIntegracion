# Generated by Django 4.1.5 on 2023-01-31 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robotAnfibio', '0007_usuarioanfibio_tipo_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='InspeccionesAnfibio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_inspeccion', models.CharField(blank=True, max_length=32, null=True)),
                ('ruta_fotos', models.CharField(blank=True, max_length=128, null=True)),
                ('ruta_videos', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
    ]