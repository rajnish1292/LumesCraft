# Generated by Django 3.2 on 2021-11-19 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lumes_craft', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
