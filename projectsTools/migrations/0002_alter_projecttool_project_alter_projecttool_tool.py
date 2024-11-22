# Generated by Django 5.1.3 on 2024-11-23 02:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_pined_alter_project_pro_cr_date_and_more'),
        ('projectsTools', '0001_initial'),
        ('tools', '0002_alter_tool_tl_name_alter_tool_tl_tool'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projecttool',
            name='project',
            field=models.ForeignKey(db_column='ptIDPro', error_messages={'blank': 'This field cannot be blank.', 'invalid': 'The selected project is not valid.', 'null': 'This field cannot be empty.'}, help_text='Project to which the tool belongs.', on_delete=django.db.models.deletion.CASCADE, to='projects.project', verbose_name='Project'),
        ),
        migrations.AlterField(
            model_name='projecttool',
            name='tool',
            field=models.ForeignKey(db_column='ptIDTl', error_messages={'blank': 'This field cannot be blank.', 'invalid': 'The selected tool is not valid.', 'null': 'This field cannot be empty.'}, help_text='Tool used in the project.', on_delete=django.db.models.deletion.CASCADE, to='tools.tool', verbose_name='Tool'),
        ),
    ]
