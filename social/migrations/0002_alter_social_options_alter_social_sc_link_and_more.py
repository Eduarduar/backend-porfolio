# Generated by Django 5.1.3 on 2024-11-23 02:34

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='social',
            options={'verbose_name': 'Social', 'verbose_name_plural': 'Socials'},
        ),
        migrations.AlterField(
            model_name='social',
            name='sc_link',
            field=models.URLField(error_messages={'blank': 'The Social Network Link field cannot be blank.', 'null': 'The Social Network Link field cannot be empty.'}, help_text='Link to the social network.', max_length=250, unique=True, validators=[django.core.validators.MaxLengthValidator(250, message='URL too long'), django.core.validators.RegexValidator('^\\S+$', message='Spaces are not allowed')], verbose_name='Social Network Link'),
        ),
        migrations.AlterField(
            model_name='social',
            name='sc_name',
            field=models.CharField(error_messages={'blank': 'The Social Network Name field cannot be blank.', 'null': 'The Social Network Name field cannot be empty.'}, help_text='Name of the social network.', max_length=250, unique=True, validators=[django.core.validators.MaxLengthValidator(250), django.core.validators.RegexValidator('^[a-zA-Z0-9().-]*$', 'Only letters, numbers, parentheses, hyphens, and periods are allowed')], verbose_name='Social Network Name'),
        ),
        migrations.AlterField(
            model_name='social',
            name='sc_status',
            field=models.BooleanField(default=True, error_messages={'blank': 'The Status field cannot be blank.', 'null': 'The Status field cannot be empty.'}, help_text='Status of the social network.', validators=[django.core.validators.MaxLengthValidator(1, message='Value not allowed'), django.core.validators.RegexValidator('^[01]$', message='Value not allowed')], verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='social',
            name='usuario',
            field=models.ForeignKey(db_column='scIDUs', error_messages={'blank': 'The User field cannot be blank.', 'invalid': 'Invalid user.', 'null': 'The User field cannot be empty.'}, help_text='User to whom the social network belongs.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]