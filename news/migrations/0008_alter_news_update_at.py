# Generated by Django 4.2.7 on 2023-11-02 14:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_news_update_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='update_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 2, 20, 44, 6, 931757)),
        ),
    ]
