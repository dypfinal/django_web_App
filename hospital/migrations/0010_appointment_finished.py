# Generated by Django 3.1.5 on 2021-05-02 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0009_auto_20210501_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]