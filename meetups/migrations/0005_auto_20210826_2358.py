# Generated by Django 3.2.6 on 2021-08-26 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0004_alter_meetup_participants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='last_name',
        ),
    ]
