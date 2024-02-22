# Generated by Django 4.2.9 on 2024-02-22 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0006_userprofile_membership'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userleaderboard',
            name='userID',
        ),
        migrations.AddField(
            model_name='membership',
            name='userID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='myapi.userprofile'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='rank',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
