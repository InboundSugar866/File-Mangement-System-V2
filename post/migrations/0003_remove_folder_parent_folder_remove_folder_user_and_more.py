# Generated by Django 5.1.4 on 2025-01-09 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_remove_file_thumbnail_alter_file_filepath'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='parent_folder',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='user',
        ),
        migrations.DeleteModel(
            name='FileFolder',
        ),
        migrations.DeleteModel(
            name='Folder',
        ),
    ]