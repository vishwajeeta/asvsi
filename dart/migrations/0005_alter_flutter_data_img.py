# Generated by Django 4.0 on 2022-08-26 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dart', '0004_alter_flutter_data_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flutter_data',
            name='img',
            field=models.ImageField(null=True, upload_to='alexander'),
        ),
    ]