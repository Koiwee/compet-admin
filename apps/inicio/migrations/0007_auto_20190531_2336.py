# Generated by Django 2.0 on 2019-06-01 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0006_jornada_btn_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competicion',
            name='descripcion',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='competicion',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='responsable',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='nom_eq1',
            field=models.CharField(default='Nombre equipo', max_length=50),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='nom_eq2',
            field=models.CharField(default='Nombre equipo', max_length=50),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='victoria',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='posicion',
            field=models.CharField(max_length=30),
        ),
    ]
