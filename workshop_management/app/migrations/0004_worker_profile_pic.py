# Generated by Django 4.1.7 on 2023-03-24 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_customer_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='profile_pic',
            field=models.FileField(default=1, upload_to='documents/'),
            preserve_default=False,
        ),
    ]