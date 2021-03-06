# Generated by Django 3.2 on 2021-11-19 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lumes_craft', '0004_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='fabric_color',
            fields=[
                ('fabric_id', models.AutoField(primary_key=True, serialize=False)),
                ('color_name', models.CharField(blank=True, max_length=500)),
                ('color_image', models.ImageField(upload_to='home/rajnish/Music/lumes_craft/lumescraft/media/fabric')),
            ],
        ),
        migrations.CreateModel(
            name='frame_color',
            fields=[
                ('frame_id', models.AutoField(primary_key=True, serialize=False)),
                ('color_name', models.CharField(blank=True, max_length=500)),
                ('color_image', models.ImageField(upload_to='home/rajnish/Music/lumes_craft/lumescraft/media/frame')),
            ],
        ),
        migrations.CreateModel(
            name='wicker_color',
            fields=[
                ('wicker_id', models.AutoField(primary_key=True, serialize=False)),
                ('color_name', models.CharField(blank=True, max_length=500)),
                ('color_image', models.ImageField(upload_to='home/rajnish/Music/lumes_craft/lumescraft/media/wicker')),
            ],
        ),
    ]
