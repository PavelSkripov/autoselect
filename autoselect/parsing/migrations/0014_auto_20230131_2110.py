# Generated by Django 3.2 on 2023-01-31 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsing', '0013_auto_20230131_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analog',
            name='difference',
            field=models.JSONField(blank=True, default=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='analog',
            name='difference1',
            field=models.JSONField(blank=True, default=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='analog',
            name='difference2',
            field=models.JSONField(blank=True, default=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='analog',
            name='difference3',
            field=models.JSONField(blank=True, default=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='analog',
            name='difference4',
            field=models.JSONField(blank=True, default=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='analog',
            name='manufacture_original',
            field=models.CharField(blank=True, default=3, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='analog',
            name='marking_analog',
            field=models.CharField(blank=True, default=3, max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='analog',
            name='marking_analog1',
            field=models.CharField(blank=True, default=3, max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='analog',
            name='marking_analog2',
            field=models.CharField(blank=True, default=3, max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='analog',
            name='marking_analog3',
            field=models.CharField(blank=True, default=3, max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='analog',
            name='marking_analog4',
            field=models.CharField(blank=True, default=3, max_length=120),
            preserve_default=False,
        ),
    ]