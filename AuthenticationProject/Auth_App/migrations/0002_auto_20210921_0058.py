# Generated by Django 3.2.4 on 2021-09-20 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Auth_App', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PhoneOTP',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
