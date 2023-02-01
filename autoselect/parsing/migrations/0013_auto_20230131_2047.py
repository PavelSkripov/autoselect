# Generated by Django 3.2 on 2023-01-31 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsing', '0012_auto_20230127_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='analog',
            name='list_analog',
            field=models.ManyToManyField(to='parsing.Sensor'),
        ),
        migrations.AddField(
            model_name='analog',
            name='marking_analog1',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='analog',
            name='marking_analog2',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='analog',
            name='marking_analog3',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='analog',
            name='marking_analog4',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='analog',
            name='difference',
            field=models.JSONField(blank=True, null=True),
        ),
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
        migrations.RemoveField(
            model_name='analog',
            name='marking_analog',
        ),
        migrations.AddField(
            model_name='analog',
            name='marking_analog',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
