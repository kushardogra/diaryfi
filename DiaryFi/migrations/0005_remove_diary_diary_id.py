# Generated by Django 3.2.6 on 2021-08-31 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DiaryFi', '0004_alter_diary_diary_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diary',
            name='diary_id',
        ),
    ]