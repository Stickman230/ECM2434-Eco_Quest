# Generated by Django 4.2.9 on 2024-02-22 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0008_remove_userprofile_id_userprofile_userid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='userID',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]