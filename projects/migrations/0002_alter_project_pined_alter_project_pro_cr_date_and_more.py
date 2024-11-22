# Generated by Django 5.1.3 on 2024-11-23 02:34

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='pined',
            field=models.BooleanField(default=False, help_text='Project pined.', verbose_name='Pined'),
        ),
        migrations.AlterField(
            model_name='project',
            name='pro_cr_date',
            field=models.DateTimeField(auto_now_add=True, help_text='Project creation date and time.', verbose_name='Creation Date'),
        ),
        migrations.AlterField(
            model_name='project',
            name='pro_desc',
            field=models.TextField(error_messages={'null': 'The description field cannot be null.'}, help_text='Project description.', max_length=1500, validators=[django.core.validators.MaxLengthValidator(1500, message='Description too long')], verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='project',
            name='pro_img',
            field=models.CharField(error_messages={'null': 'The image field cannot be null.'}, help_text='Project image.', max_length=255, validators=[django.core.validators.RegexValidator(message='No spaces allowed', regex='^\\S+$'), django.core.validators.MaxLengthValidator(255, message='URL too long')], verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='project',
            name='pro_link',
            field=models.URLField(blank=True, help_text='Project link.', max_length=255, null=True, validators=[django.core.validators.MaxLengthValidator(255, message='URL too long'), django.core.validators.RegexValidator(message='No spaces allowed', regex='^\\S+$')], verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='project',
            name='pro_name',
            field=models.CharField(error_messages={'null': 'The project name field cannot be null.'}, help_text='Project name.', max_length=100, validators=[django.core.validators.MaxLengthValidator(100, message='Name too long'), django.core.validators.RegexValidator('^[a-zA-Z0-9.\\-()]*$', 'Only letters, numbers, hyphens, periods, and parentheses are allowed')], verbose_name='Project name'),
        ),
        migrations.AlterField(
            model_name='project',
            name='pro_rep',
            field=models.CharField(blank=True, help_text='Project repository.', max_length=255, null=True, validators=[django.core.validators.RegexValidator(message='No spaces allowed', regex='^\\S+$'), django.core.validators.MaxLengthValidator(255, message='URL too long')], verbose_name='Repository'),
        ),
        migrations.AlterField(
            model_name='project',
            name='pro_up_date',
            field=models.DateTimeField(blank=True, help_text='Project last update date and time.', null=True, verbose_name='Update Date'),
        ),
        migrations.AlterField(
            model_name='project',
            name='usuario',
            field=models.ForeignKey(db_column='proIDUs', error_messages={'blank': 'The user field cannot be blank.', 'invalid': 'Invalid user.', 'null': 'The user field cannot be null.'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
