# Generated by Django 3.2 on 2023-01-31 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsing', '0016_auto_20230131_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analog',
            name='difference',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='analog',
            name='difference1',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='analog',
            name='difference2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='analog',
            name='difference3',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='analog',
            name='difference4',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
