# Generated by Django 4.2.3 on 2023-07-30 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='estrenos',
            fields=[
                ('codigo', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('titulo', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('sinopsis', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='pelicula',
            fields=[
                ('codigo', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('titulo', models.CharField(max_length=100)),
                ('sinopsis', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='serie',
            fields=[
                ('codigo', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('titulo', models.CharField(max_length=100)),
                ('sinopsis', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('codigo', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('cod_peli', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pelis.pelicula')),
                ('cod_serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pelis.serie')),
            ],
        ),
    ]