# Generated by Django 3.0.7 on 2020-08-28 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_ticketinfo_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketinfo',
            name='date',
            field=models.CharField(max_length=10),
        ),
    ]
