# Generated by Django 3.0 on 2021-12-16 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20211214_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_token',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='forgot_password',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]