# Generated by Django 3.1.1 on 2021-01-11 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("founders", "0004_auto_20210111_1907"),
    ]

    operations = [
        migrations.AddField(
            model_name="progress",
            name="conversation",
            field=models.IntegerField(default=45),
        ),
        migrations.AddField(
            model_name="progress",
            name="primary_metric",
            field=models.IntegerField(default=1234),
        ),
    ]
