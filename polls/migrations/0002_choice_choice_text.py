# Generated by Django 2.0.2 on 2020-03-09 04:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(default=datetime.datetime(2020, 3, 9, 4, 58, 28, 895959, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
