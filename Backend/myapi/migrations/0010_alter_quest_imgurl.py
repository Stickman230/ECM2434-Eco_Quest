# Generated by Django 4.2.9 on 2024-02-29 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0009_quest_imgurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='imgURL',
            field=models.CharField(max_length=200),
        ),
    ]
