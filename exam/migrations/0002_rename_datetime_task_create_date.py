# Generated by Django 4.2.3 on 2023-07-26 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='datetime',
            new_name='create_date',
        ),
    ]
