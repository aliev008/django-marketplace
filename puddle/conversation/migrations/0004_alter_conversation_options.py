# Generated by Django 4.2.7 on 2023-11-20 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0003_alter_conversationmessages_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conversation',
            options={'ordering': ('-modified_at',)},
        ),
    ]