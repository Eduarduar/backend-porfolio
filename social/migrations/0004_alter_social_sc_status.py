# Generated by Django 5.1.3 on 2024-11-23 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_alter_social_sc_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='sc_status',
            field=models.BooleanField(default=True, error_messages={'blank': 'The Status field cannot be blank.', 'null': 'The Status field cannot be empty.'}, help_text='Status of the social network.', verbose_name='Status'),
        ),
    ]
