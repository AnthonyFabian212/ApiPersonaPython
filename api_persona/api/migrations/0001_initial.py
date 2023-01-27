# Generated by Django 4.1.3 on 2023-01-26 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('cedula', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('monto_primera_compra', models.FloatField()),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.tipo_persona')),
            ],
        ),
    ]
