# Generated by Django 5.1.7 on 2025-03-30 14:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_details',
            name='task',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='tasks.task'),
        ),
    ]
