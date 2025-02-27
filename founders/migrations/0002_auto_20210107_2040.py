# Generated by Django 3.1.1 on 2021-01-07 20:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("founders", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="founder",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="founder",
                to=settings.AUTH_USER_MODEL,
                unique=True,
            ),
        ),
    ]
