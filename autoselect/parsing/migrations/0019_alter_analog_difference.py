# Generated by Django 3.2 on 2023-01-31 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsing', '0018_auto_20230131_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analog',
            name='difference',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
