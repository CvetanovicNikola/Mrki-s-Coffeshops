# Generated by Django 2.1.3 on 2019-03-10 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffeshop', '0002_auto_20190310_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffeeshop',
            name='description2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='coffeeshop',
            name='description3',
            field=models.TextField(blank=True),
        ),
    ]