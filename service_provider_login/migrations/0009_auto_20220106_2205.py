# Generated by Django 3.2.9 on 2022-01-06 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_provider_login', '0008_alter_servicecreds_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicecreds',
            name='details',
            field=models.CharField(default='We are great at what we do!', max_length=300),
        ),
        migrations.AlterField(
            model_name='servicecreds',
            name='service',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='servicecreds',
            name='user_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
