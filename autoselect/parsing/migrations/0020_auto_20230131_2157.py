# Generated by Django 3.2 on 2023-01-31 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsing', '0019_alter_analog_difference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analog',
            name='difference1',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='analog',
            name='difference2',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='analog',
            name='difference3',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='analog',
            name='difference4',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
