# Generated by Django 4.2.3 on 2023-07-30 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pelis', '0002_estrenos_imagen_pelicula_imagen_serie_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='estrenos',
            name='tipo',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]