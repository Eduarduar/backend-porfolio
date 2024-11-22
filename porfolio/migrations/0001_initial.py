# Generated by Django 5.1.3 on 2024-11-23 00:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id_us', models.AutoField(primary_key=True, serialize=False)),
                ('us_fr_name', models.CharField(max_length=30)),
                ('us_ls_name', models.CharField(blank=True, max_length=50, null=True)),
                ('us_email', models.EmailField(max_length=254, unique=True)),
                ('us_phone', models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(message="El número de teléfono debe estar en el formato '+52 1234567890'.", regex='^\\+52 \\d{10}$')])),
                ('us_br_date', models.DateField()),
                ('us_photo', models.CharField(blank=True, default='static/users/placeholder.jpg', max_length=255, null=True)),
                ('us_cr_date', models.DateTimeField(auto_now_add=True)),
                ('us_up_date', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'USUARIOS',
            },
        ),
    ]
