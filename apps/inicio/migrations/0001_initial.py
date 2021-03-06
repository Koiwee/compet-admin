# Generated by Django 2.0 on 2019-05-28 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Competicion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=400)),
                ('programado', models.BooleanField()),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('escudo', models.ImageField(upload_to='img_escudos')),
                ('responsable', models.CharField(max_length=100)),
                ('creacion', models.DateField()),
                ('competicion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.Competicion')),
            ],
        ),
        migrations.CreateModel(
            name='Jornada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('ptsEq1', models.IntegerField(blank=True, null=True)),
                ('ptsEq2', models.IntegerField(blank=True, null=True)),
                ('victoria', models.CharField(max_length=100)),
                ('equipo1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='local', to='inicio.Equipo')),
                ('equipo2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foraneo', to='inicio.Equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('posicion', models.CharField(max_length=50)),
                ('dorsal', models.CharField(max_length=3)),
                ('foto', models.ImageField(upload_to='img_jugadores')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.Equipo')),
            ],
        ),
    ]
