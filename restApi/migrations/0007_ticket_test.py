# Generated by Django 5.0.1 on 2024-01-23 12:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restApi", "0006_necessarytickets"),
    ]

    operations = [
        migrations.AddField(
            model_name="ticket",
            name="test",
            field=models.ManyToManyField(to="restApi.ticket"),
        ),
    ]