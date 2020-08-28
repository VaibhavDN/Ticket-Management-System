# Generated by Django 3.0.7 on 2020-08-28 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20200828_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketinfo',
            name='expired',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ticketinfo',
            name='movieName',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='ticketinfo',
            name='time_seconds',
            field=models.IntegerField(default=0),
        ),
    ]
