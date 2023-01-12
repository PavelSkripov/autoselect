# Generated by Django 3.2 on 2023-01-12 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parsing', '0003_auto_20230111_2330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analog',
            name='marking_analog',
        ),
        migrations.AddField(
            model_name='analog',
            name='marking_analog',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='parsing.sensor'),
            preserve_default=False,
        ),
    ]
