# Generated by Django 3.1.4 on 2021-01-21 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('batches', '0002_auto_20210121_1623'),
    ]

    operations = [
        migrations.RenameField(
            model_name='batches',
            old_name='Message',
            new_name='message',
        ),
    ]
