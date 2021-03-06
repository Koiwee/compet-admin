# Generated by Django 2.0 on 2019-05-31 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_auto_20190528_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jornada',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='victoria',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='img_jugadores'),
        ),
    ]
