# Generated by Django 4.2.3 on 2023-07-26 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_alter_task_create_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['is_done', '-create_date']},
        ),
    ]
