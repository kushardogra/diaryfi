# Generated by Django 3.2.6 on 2021-08-31 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DiaryFi', '0005_remove_diary_diary_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='diary_id',
            field=models.CharField(auto_created=5, max_length=5, null=True),
        ),
    ]