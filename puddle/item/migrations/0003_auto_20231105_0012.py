# Generated by Django 3.2.12 on 2023-11-05 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_auto_20231105_0004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='iamge',
        ),
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='item_images'),
        ),
    ]