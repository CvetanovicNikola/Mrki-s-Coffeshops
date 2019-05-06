# Generated by Django 2.1.3 on 2019-03-10 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('text', models.TextField()),
                ('date', models.DateTimeField()),
                ('title', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='User_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
