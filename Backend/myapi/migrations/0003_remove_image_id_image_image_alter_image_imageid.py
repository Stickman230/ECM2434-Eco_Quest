# Generated by Django 4.2.9 on 2024-02-26 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='id',
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='imageID',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]