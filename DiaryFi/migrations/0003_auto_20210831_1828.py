# Generated by Django 3.2.6 on 2021-08-31 12:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DiaryFi', '0002_dairy_contents_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='diary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diary_id', models.CharField(max_length=11, null=True)),
                ('diary_name', models.CharField(max_length=500, null=True)),
                ('content', models.CharField(max_length=10000, null=True)),
                ('photo', models.FileField(max_length=10000, null=True, upload_to='')),
                ('Date', models.DateTimeField(default=datetime.datetime.now, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='dairy_contents',
        ),
    ]
