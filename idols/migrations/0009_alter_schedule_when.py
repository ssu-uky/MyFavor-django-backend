# Generated by Django 4.1.7 on 2023-03-22 09:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idols', '0008_alter_schedule_when'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='when',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 22, 9, 19, 31, 890049, tzinfo=datetime.timezone.utc)),
        ),
    ]
