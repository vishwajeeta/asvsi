# Generated by Django 4.0 on 2022-06-03 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_diarydata_dates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diarydata',
            name='content',
            field=models.TextField(max_length=5000),
        ),
    ]