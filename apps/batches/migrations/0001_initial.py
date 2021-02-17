# Generated by Django 3.1.4 on 2021-01-21 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('batches', models.PositiveIntegerField(max_length=2)),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=100)),
                ('Message', models.TextField(max_length=25)),
            ],
        ),
    ]
