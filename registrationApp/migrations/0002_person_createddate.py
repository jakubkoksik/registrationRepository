# Generated by Django 4.0.2 on 2022-04-26 20:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('registrationApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='createdDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
