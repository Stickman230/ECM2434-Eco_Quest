# Generated by Django 4.2.7 on 2024-03-24 12:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapi", "0007_alter_quest_date_made_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quest",
            name="date_made_active",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 24, 0, 0), null=True
            ),
        ),
    ]
