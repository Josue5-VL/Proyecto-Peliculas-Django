# Generated by Django 4.2.3 on 2023-07-30 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pelis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estrenos',
            name='imagen',
            field=models.ImageField(null=True, upload_to='pelis/static/media'),
        ),
        migrations.AddField(
            model_name='pelicula',
            name='imagen',
            field=models.ImageField(null=True, upload_to='pelis/static/media'),
        ),
        migrations.AddField(
            model_name='serie',
            name='imagen',
            field=models.ImageField(null=True, upload_to='pelis/static/media'),
        ),
    ]
