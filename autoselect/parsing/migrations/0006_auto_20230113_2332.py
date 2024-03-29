# Generated by Django 3.2 on 2023-01-13 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsing', '0005_auto_20230112_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='analog',
            name='difference1',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='analog',
            name='difference2',
            field=models.TextField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensor',
            name='sens_type',
            field=models.CharField(default=3, max_length=60),
            preserve_default=False,
        ),
    ]
