# Generated by Django 3.1.1 on 2021-01-14 18:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("founders", "0009_auto_20210114_0632"),
    ]

    operations = [
        migrations.AlterField(
            model_name="progress",
            name="end_date",
            field=models.CharField(default=datetime.date(2021, 1, 17), max_length=255),
        ),
    ]
