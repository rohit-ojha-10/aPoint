# Generated by Django 3.2.9 on 2022-01-06 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_provider_login', '0002_servicecreds_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicecreds',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to=None),
        ),
    ]
