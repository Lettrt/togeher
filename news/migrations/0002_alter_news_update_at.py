# Generated by Django 4.2.7 on 2023-11-02 12:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='update_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 2, 18, 57, 29, 985644)),
        ),
    ]