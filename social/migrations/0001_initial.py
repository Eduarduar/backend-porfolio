# Generated by Django 5.1.3 on 2024-11-23 00:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sc_name', models.CharField(max_length=250, unique=True)),
                ('sc_link', models.URLField(max_length=250, unique=True)),
                ('sc_status', models.BooleanField(default=True)),
                ('usuario', models.ForeignKey(db_column='scIDUs', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Social',
                'verbose_name_plural': 'Sociales',
                'db_table': 'SOCIAL',
            },
        ),
    ]