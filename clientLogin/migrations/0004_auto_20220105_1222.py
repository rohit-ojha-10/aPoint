# Generated by Django 3.2.9 on 2022-01-05 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientLogin', '0003_rename_user_name_consumercreds_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicecreds',
            name='details',
            field=models.CharField(default='We are great at what we do!', max_length=100),
        ),
        migrations.AddField(
            model_name='servicecreds',
            name='total_slots',
            field=models.IntegerField(default=0),
        ),
    ]
