# Generated by Django 3.2.9 on 2022-01-06 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_provider_login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicecreds',
            name='image',
            field=models.ImageField(default=None, upload_to=None),
        ),
    ]
