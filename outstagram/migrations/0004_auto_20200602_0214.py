# Generated by Django 2.2.10 on 2020-06-01 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outstagram', '0003_auto_20200601_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_name',
            field=models.CharField(default='default', max_length=30),
        ),
    ]
