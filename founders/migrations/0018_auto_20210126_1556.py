# Generated by Django 3.1.1 on 2021-01-26 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('founders', '0017_auto_20210126_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progress',
            name='learning_stakeholder',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='progress',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='progress',
            name='target_market',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='progress',
            name='top_priorities',
            field=models.TextField(null=True),
        ),
    ]
