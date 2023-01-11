# Generated by Django 3.2 on 2023-01-11 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marking', models.CharField(max_length=120)),
                ('case_size', models.CharField(max_length=60)),
                ('mounting', models.CharField(max_length=60)),
                ('sensing_distance', models.CharField(max_length=60)),
                ('connection_type', models.CharField(max_length=60)),
                ('housing', models.CharField(max_length=60)),
                ('diameter', models.CharField(max_length=60)),
                ('length', models.CharField(max_length=60)),
                ('type_shell', models.CharField(max_length=60)),
                ('size_frame', models.CharField(max_length=60)),
                ('current', models.CharField(max_length=60)),
                ('voltage', models.CharField(max_length=60)),
                ('contact_structure', models.CharField(max_length=60)),
                ('frequency', models.CharField(max_length=60)),
                ('indication', models.CharField(max_length=60)),
                ('electr_protection', models.CharField(max_length=60)),
                ('degree_of_protect', models.CharField(max_length=60)),
                ('num_wires', models.IntegerField(max_length=60)),
                ('temp_range', models.CharField(max_length=60)),
                ('work_dist', models.CharField(max_length=60)),
                ('special', models.CharField(max_length=60)),
                ('wiring', models.CharField(max_length=60)),
                ('manufacture', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Analog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marking_original', models.CharField(max_length=120)),
                ('difference', models.TextField()),
                ('manufacture_original', models.CharField(max_length=60)),
                ('marking_analog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parsing.sensor')),
            ],
        ),
    ]