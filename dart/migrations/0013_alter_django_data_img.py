# Generated by Django 4.0 on 2022-11-21 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dart', '0012_django_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='django_data',
            name='img',
            field=models.ImageField(default='defaults.jpg', null=True, upload_to='python'),
        ),
    ]