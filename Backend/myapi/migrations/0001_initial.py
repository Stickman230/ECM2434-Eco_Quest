# Generated by Django 5.0.1 on 2024-03-24 19:23

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('imageID', models.BigAutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='images/')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('locationID', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='QuestType',
            fields=[
                ('questTypeID', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80, unique=True)),
                ('description', models.CharField(default='', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Society',
            fields=[
                ('societyID', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(default='', max_length=150)),
                ('numberOfMembers', models.PositiveBigIntegerField(default=0)),
                ('societyXP', models.PositiveBigIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Societies',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField(choices=[('Player', 'Player'), ('GameKeeper', 'GameKeeper'), ('Developer', 'Developer')], default='Player', max_length=20)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('bio', models.CharField(default='', max_length=150)),
                ('rank', models.PositiveIntegerField(default=1)),
                ('XP', models.PositiveIntegerField(default=0)),
                ('streak', models.PositiveIntegerField(default=0)),
                ('border', models.CharField(default='none', max_length=100)),
                ('imgURL', models.CharField(default='none', max_length=200)),
                ('is_active', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends_user1', to=settings.AUTH_USER_MODEL)),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends_user2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('questID', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('task', models.CharField(default='', max_length=150)),
                ('reward', models.PositiveBigIntegerField(default=0)),
                ('state', models.BooleanField(default=False)),
                ('imgURL', models.CharField(max_length=200)),
                ('date_made_active', models.DateTimeField(default=None, null=True)),
                ('locationID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('questTypeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.questtype')),
            ],
        ),
        migrations.CreateModel(
            name='QuestSubmission',
            fields=[
                ('questsubID', models.BigAutoField(primary_key=True, serialize=False)),
                ('imgURL', models.CharField(max_length=200)),
                ('info', models.CharField(default='The task has been completed', max_length=150)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('verified', models.BooleanField(default=False)),
                ('rejected', models.BooleanField(default=False)),
                ('questID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.quest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('membershipID', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('since', models.DateField(auto_now_add=True)),
                ('state', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('societyID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapi.society')),
            ],
        ),
    ]
