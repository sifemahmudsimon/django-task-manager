# Generated by Django 5.0 on 2023-12-27 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_remove_task_task_complete_task_taskstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='taskstatus',
            field=models.CharField(choices=[('active', 'Active'), ('complete', 'Complete')], max_length=10),
        ),
    ]
