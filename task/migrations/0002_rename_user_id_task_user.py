# Generated by Django 4.2.1 on 2023-06-09 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='user_id',
            new_name='user',
        ),
    ]
