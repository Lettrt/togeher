# Generated by Django 4.2.7 on 2023-11-02 14:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_alter_news_update_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='update_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 2, 20, 43, 26, 902430)),
        ),
    ]
