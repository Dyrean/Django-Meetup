# Generated by Django 3.2.6 on 2021-08-26 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0003_alter_meetup_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetup',
            name='participants',
            field=models.ManyToManyField(blank=True, null=True, related_name='participants', to='meetups.Participant'),
        ),
    ]
