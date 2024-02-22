# Generated by Django 4.2.9 on 2024-02-22 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestType',
            fields=[
                ('questTypeID', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('questID', models.BigAutoField(primary_key=True, serialize=False)),
                ('quest_name', models.CharField(max_length=50)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('Task', models.CharField(max_length=150)),
                ('state', models.BooleanField(default=False)),
                ('questTypeID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapi.questtype')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapi.user')),
            ],
        ),
    ]
