# Generated by Django 2.0 on 2019-05-31 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_auto_20190530_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='jornada',
            name='competicion',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='inicio.Competicion'),
            preserve_default=False,
        ),
    ]